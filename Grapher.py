class Grapher:

  def __init__(self, events):
    self.data = {
      'mouse_movements': [],
      'mouse_clicks': [],
      'mouse_scrolls': [],
      'key_presses': [],
      'key_releases': []
    }
    for event in events:
      if event['type'] == 'mm':
        self.data['mouse_movements'].append(event)
      elif event['type'] == 'ms':
        self.data['mouse_scrolls'].append(event)
      elif event['type'] == 'mc':
        self.data['mouse_clicks'].append(event)
      elif event['type'] == 'kp':
        self.data['key_presses'].append(event)
      elif event['type'] == 'kr':
        self.data['key_releases'].append(event)
      else:
        pass