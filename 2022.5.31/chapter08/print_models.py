import printing_functions as pf

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# [:] 创建列表副本
pf.print_models(unprinted_designs[:], completed_models)
pf.show_completed_models(completed_models)
