#Bayes Theorem
def get_outcomes(sample_space, f_name='', e_name=''):
    outcomes = 0
    for e_k, e_v in sample_space.items():
        if f_name=='' or f_name==e_k:
            for se_k, se_v in e_v.items():
                if e_name!='' and se_k == e_name:
                    outcomes+=se_v
                elif e_name=='':
                    outcomes+=se_v
    return outcomes

def p(sample_space, f_name):
    return get_outcomes(sample_space, f_name) / get_outcomes(sample_space, '', '')

def p_inters(sample_space, f_name, e_name):
    return get_outcomes(sample_space, f_name, e_name) / get_outcomes(sample_space, '', '')

def p_conditional(sample_space, f_name, e_name):
    return p_inters(sample_space, f_name, e_name) / p(sample_space, f_name)

def bayes(sample_space, f, given_e):
    sum = 0;
    for e_k, e_v in sample_space.items():
        sum+=p(sample_space, e_k) * p_conditional(sample_space, e_k, given_e)
    return p(sample_space, f) * p_conditional(sample_space, f, given_e) / sum

sample_space = {'UK':{'Boy':10, 'Girl':20},
                'FR':{'Boy':10, 'Girl':10},
                'CA':{'Boy':10, 'Girl':30}}

print('Probability of being from FR:', p(sample_space, 'FR'))
print('Probability to be French Boy:', p_inters(sample_space, 'FR', 'Boy'))
print('Probability of being a Boy given a person is from FR:', p_conditional(sample_space, 'FR', 'Boy'))
print('Probability to be from France given person is Boy:', bayes(sample_space, 'FR', 'Boy'))


sample_space = {'Grow' :{'Up':160, 'Down':40},
                'Slows':{'Up':30, 'Down':70}}

print('Probability economy is growing when stock is Up:', bayes(sample_space, 'Grow', 'Up'))




