
class FIFO:
    def __init__(self,page_reference_string,page_frame_size,window_size):
      self.page_reference_string = page_reference_string
      self.page_frame_size = page_frame_size
      self.window_size = window_size
      self.InOut_number = len(self.page_reference_string) - self.page_frame_size

    def show(self):
      
      # memory state 를 저장하는 list
      # 현재 page referene string 의 위치를 나타내는 pointer
      # page fault 를 체크하는 list
      memory_state = [ [ self.page_reference_string[i] for i in range(self.page_frame_size) ] ]
      pointer = self.page_frame_size
      page_fault_check = []

      # page frame 이 다 차기 시작하고 나서부터의 상황을 가정으로 한다.
      for i in range(self.InOut_number):
  
        if self.page_reference_string[pointer] in memory_state[i]:
          page_fault_check.append(0)
          memory_state.append(memory_state[i])
    
        else:
          page_fault_check.append(1)
          swapout = memory_state[i][1:]
          swapout.append(self.page_reference_string[pointer])
          memory_state.append(swapout)
          
        pointer += 1

        if pointer >= len(self.page_reference_string):
          break

      # 초기 메모리 상태는 비어있는 것으로 가정하므로 page frame 이 다 차기 이전의 page fault 도 채워준다.
      for i in range(len(self.page_reference_string) - self.InOut_number):
        page_fault_check.insert(0, 1)
      
      # 초기 메모리 상태는 비어있는 것으로 가정하므로 page frame 이 다 차기 이전의 memory state 도 넣어준다.
      for i in range(len(self.page_reference_string) - self.InOut_number - 1):
        memory_state.insert(i, self.page_reference_string[:i+1])
      

      return memory_state, page_fault_check

      
      