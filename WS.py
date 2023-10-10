class WS:
    def __init__(self,page_reference_string,page_frame_size,window_size):
      self.page_reference_string = page_reference_string
      self.page_frame_size = page_frame_size
      self.window_size = window_size
      self.InOut_number = len(self.page_reference_string) - self.window_size

    def show(self):

      # memory state 를 저장하는 list
      # 현재 page referene string 의 위치를 나타내는 pointer
      # page fault 를 체크하는 list
      memory_state = [ [ self.page_reference_string[i] for i in range(self.window_size) ] ]
      pointer = self.page_frame_size
      page_fault_check = []

      for i in range(self.InOut_number):
  
        if self.page_reference_string[pointer] in memory_state[i]:
          page_fault_check.append(0)
          memory_state.append(self.page_reference_string[i+1:i+1+self.window_size])
    
        else:
          page_fault_check.append(1)
          memory_state.append(self.page_reference_string[i+1:i+1+self.window_size])
          
        pointer += 1

        if pointer >= len(self.page_reference_string):
          break
      
      # 맨 처음 데이터가 메모리에 들어올 때의 page fault 까지 더해준다. 
      page_fault_check.insert(0,1)

      return memory_state, page_fault_check
