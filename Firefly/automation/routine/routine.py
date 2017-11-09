from Firefly import logging
from Firefly.automation.const import AUTOMATION_INTERFACE
from Firefly.automation.routine.const import ROUTINE_EXECUTE, ROUTINE_ICON, ROUTINE_MODE, ROUTINE_ROUTINE
from Firefly.automation.routine.metadata import METADATA, TITLE
from Firefly.const import COMMAND_NOTIFY, SERVICE_NOTIFICATION, TYPE_ROUTINE
from Firefly.helpers.automation import Automation
from Firefly.helpers.events import Command, Event


# TODO: Routines should take a list of lights to turn off and a list of lights to user definable value.


def Setup(firefly, package, **kwargs):
  logging.message('Entering %s setup Routine' % package)
  if not kwargs.get('interface'):
    kwargs['interface'] = {}
  # if kwargs.get('metadata'):
  #  METADATA.update(kwargs['metadata'])
  kwargs['metadata'] = METADATA
  routine = Routine(firefly, package, **kwargs)
  return firefly.install_component(routine)


class Routine(Automation):
  def __init__(self, firefly, package, **kwargs):
    super().__init__(firefly, package, self.event_handler, **kwargs)

    # TODO(zpriddy): Fix this is firebase service
    self._title = TITLE
    self._package = self.package
    self._alias = self.alias

    #TODO: Change these to self.interface.settings.mode and interface.settings.icon
    self.mode = self.new_interface.mode.get(ROUTINE_ROUTINE, None)
    self.icon = self.new_interface.icon.get(ROUTINE_ROUTINE, '')
    self.export_ui = self.new_interface.export_ui.get(ROUTINE_ROUTINE, True)


    # TODO: replace export_ui with a const from metadata or core.
    #self.export_ui = self.interface.get('export_ui', {}).get(ROUTINE_ROUTINE, True)

    self.add_command(ROUTINE_EXECUTE, self.event_handler)

  def export(self, **kwargs):
    if kwargs.get('firebase_view'):
      return self.get_view(**kwargs)

    export_data = super().export()
    export_data[AUTOMATION_INTERFACE][ROUTINE_ICON] = {
      ROUTINE_ROUTINE: self.icon
    }
    # TODO: replace export_ui with a const from metadata or core.
    export_data[AUTOMATION_INTERFACE]['export_ui'] = {
      ROUTINE_ROUTINE: self.export_ui
    }
    if self.mode:
      export_data[AUTOMATION_INTERFACE][ROUTINE_MODE] = {
        ROUTINE_ROUTINE: self.mode
      }

    return export_data

  def get_view(self, **kwargs):
    view_data = {
      'ff_id':     self.id,
      'alias':     self.alias,
      'icon':      self.icon,
      'command':   'execute',
      'export_ui': self.export_ui
    }
    return view_data

  def event_handler(self, event: Event = None, trigger_index=0, **kwargs):
    if self.new_interface.messages.get(ROUTINE_ROUTINE):
      notify = Command(SERVICE_NOTIFICATION, self.id, COMMAND_NOTIFY, message=self.new_interface.messages.get(ROUTINE_ROUTINE))
      self.firefly.send_command(notify)

    if self.mode:
      self.firefly.location.mode = self.mode

    if self.new_interface.actions.get(ROUTINE_ROUTINE):
      for a in self.new_interface.actions.get(ROUTINE_ROUTINE):
        a.execute_action(self.firefly)
    return True

  def get_alexa_view(self, **kwargs):
    if self.export_ui is False:
      return None

    return {
      'endpointId':        self.id,
      'manufacturerName':  'Firefly Home',
      'friendlyName':      self.alias,
      'description':       'A Firefly Home Scene',
      'displayCategories': ['SCENE_TRIGGER'],
      'cookie':            {},
      'capabilities':      [
        {
          'type':                 'AlexaInterface',
          'interface':            'Alexa.SceneController',
          'version':              '3',
          'supportsDeactivation': False,
          'proactivelyReported':  True
        }
      ]
    }

  @property
  def type(self):
    return TYPE_ROUTINE