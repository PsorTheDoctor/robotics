#!/usr/bin/python

import numpy as np
import rospy
from kair_universalrobot.srv import MovePTP_P, MovePTP_PRequest
from kair_evg55.srv import Open, OpenRequest


def grasp(opened):
	service = '/kair_evg55_2/open'
	rospy.wait_for_service(service)
	try:
		moveGripper = rospy.ServiceProxy(service, Open)
		return moveGripper(50 if opened else 0)
	except rospy.ServiceException as e:
		print('Service call failed: %s'%e)


def move(array):
	service = '/ur5_1/move_ptp_p'
	
	if len(array) == 6:
		rospy.wait_for_service(service)
		try:
			movePtp = rospy.ServiceProxy(service, MovePTP_P)
			req = MovePTP_PRequest()
			req.target.data = array
			req.a = 1
			req.v = 1
			req.t = 5
			req.r = 0
			resp = movePtp(req)
			print('Success')
			return resp
		except rospy.ServiceException as e:
			print('Service call failed: %s'%e)
	else:
		print('Array length must be 6')


if __name__ == '__main__':
	# move([-0.3, 0.2, 0.5, 0.0, 2.22, -2.22])
	grasp(False)
