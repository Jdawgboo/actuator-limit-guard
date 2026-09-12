def check(current:float,target:float,minimum:float,maximum:float,max_step:float)->list[str]:
 errors=[]
 if not minimum<=target<=maximum: errors.append('out_of_range')
 if abs(target-current)>max_step: errors.append('step_too_large')
 return errors
