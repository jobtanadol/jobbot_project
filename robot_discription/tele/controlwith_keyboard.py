import rospy
from geometry_msgs.msg import Twist

def controlwith_key():

    rospy.init_node('controlwith_keyboard_node')
    
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)
    T = Twist()

    velocity = 0.0
    T.linear.y = 0.0
    T.linear.z = 0.0
    T.angular.x = 0.0
    T.angular.y = 0.0
    print("select your gear")
    print("gear 1 : velocity : 0.1")
    print("gear 2 : velocity : 0.2")
    print("gear 3 : velocity : 0.3")
    gear = input("select gear : ")
    if gear=='1':
    	velocity=0.1
    elif gear=='2':
    	velocity=0.2
    elif gear=='3':
    	velocity=0.3
    else:
        pass

    while(1):
        kb = input("press any key : ")
        if kb == 'w':
            T.linear.x = velocity
            T.angular.z = 0.0
            print("go forward")
        elif kb == 's':
            T.linear.x = -velocity
            T.angular.z = 0.0
            print("go backward")
        elif kb == 'a':
            T.angular.z = -velocity
            print("go left")
        elif kb == 'd':
            T.angular.z = velocity
            print("go right")
        elif kb == ' ':
            T.linear.x = 0.0
            T.angular.z = 0.0
            print(" break ")
        elif kb=='q':
            T.linear.x = 0.0
            T.angular.z = 0.0
            pub.publish(T)
            print(" Quit ")
            break
        else :
            pass

        pub.publish(T)
        rate.sleep()

if __name__=="__main__":
    try:
        controlwith_key()
    except rospy.ROSInterruptException:
        pass
