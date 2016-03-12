	# /* Convert sync type to SynchroTrace's expected value
	# 	 * From SynchroTraceSim source code:
	# 	 *
	# 	 * #define P_MUTEX_LK              1
	# 	 * #define P_MUTEX_ULK             2
	# 	 * #define P_CREATE                3
	# 	 * #define P_JOIN                  4
	# 	 * #define P_BARRIER_WT            5
	# 	 * #define P_COND_WT               6
	# 	 * #define P_COND_SG               7
	# 	 * #define P_SPIN_LK               8
	# 	 * #define P_SPIN_ULK              9
	# 	 * #define P_SEM_INIT              10
	# 	 * #define P_SEM_WAIT              11
	# 	 * #define P_SEM_POST              12
	# 	 * #define P_SEM_GETV              13
	# 	 * #define P_SEM_DEST              14
	# 	 *
	# 	 * NOTE: semaphores are not supported in SynchroTraceGen
	# 	 */

from event import Event
class Synchronization(Event):

    def __init__(self, eventNumber, threadId, pthread_call_type, address_of_synchronization_structure):
        Event.__init__(self, eventNumber, threadId)
        self.pthread_call_type = pthread_call_type
        self.address_of_synchronization_structure = address_of_synchronization_structure

    def getPthreadCallType(self):
        return self.pthread_call_type

    def getSyncStructAddress(self):
        return self.address_of_synchronization_structure
