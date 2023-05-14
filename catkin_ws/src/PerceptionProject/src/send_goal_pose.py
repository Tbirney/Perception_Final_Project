import rospy
from actionlib import SimpleActionClient
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Pose, Point, Quaternion
from tf.transformations import quaternion_from_euler

def send_goal_pose():

    pos = [2, 1]

    rospy.init_node('send_goal_pose')

    # movebase is the thing that will actually move the turtlebot
    move_client = SimpleActionClient('move_base', MoveBaseAction)
    move_client.wait_for_server()

    # https://www.programcreek.com/python/example/113987/move_base_msgs.msg.MoveBaseGoal
    # this page taks about how to set the goal pose
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = 'map'
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = pos[0]
    goal.target_pose.pose.position.y = pos[1]


    # need to normalize quarternion
    # forum https://answers.ros.org/question/28819/quaternion-has-length-close-to-zero-discarding-as-navigation-goal-why/
    # solution https://hotblackrobotics.github.io/en/blog/2018/01/29/seq-goals-py/
    quat = Quaternion(*quaternion_from_euler(0, 0, 1.57))
    goal.target_pose.pose.orientation = quat
    # quaternionArray = tf.transformations.quaternion_about_axis(0, (0,0,1))
    # goal.target_pose.pose.orientation = self.array_to_quaternion(quaternionArray)
    move_client.send_goal(goal)


    wait = move_client.wait_for_result()
    if not wait:
        rospy.signal_shutdown("Error connecting to move base server")
    else:
        return move_client.get_result()

# If the python node is executed as main process (sourced directly)
if __name__ == '__main__':
    try:
        result = send_goal_pose()
    except rospy.ROSInterruptException:
        rospy.loginfo("No Result from navigation")

