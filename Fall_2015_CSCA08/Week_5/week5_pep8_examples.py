def is_accepted(program_code,gpa,name):
    csc_accepted =(program_code=='CSC')
    mat_sta_accepted= (((program_code=='MAT')or(program_code == 'STA'))and(gpa>=3))
    non_cms_accepted = (gpa> 3.5)
    name_accepted =(name=='Brian')
    result = (csc_accepted or mat_sta_accepted or non_cms_accepted or name_accepted)
    return result

# non-pep-8 example ¡ü, pep-8 example ¡ý

def is_accepted(program_code, gpa, name):
    csc_accepted = (program_code == 'CSC')
    mat_sta_accepted = (((program_code == 'MAT') or (program_code == 'STA')
                         ) and (gpa >= 3))
    non_cms_accepted = (gpa > 3.5)
    name_accepted = (name == 'Brian')
    result = (csc_accepted or mat_sta_accepted or
              non_cms_accepted or name_accepted)
    return result
