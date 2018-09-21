from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.actions import Action
from rasa_core.events import SlotSet
class ActionDegreeInfo(Action):
    def name(self):
    #     return 'action_degreeinfo'
    # def run(self):
        # print(u'Thanks for the enquiry. :)')
		print(u'Thank you for enquiry, any thing else you want to know?')
		return 'action_degreeinfo'
        # pass