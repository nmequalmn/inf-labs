import xmlplain

with open("./input.xml") as f:
  root = xmlplain.xml_to_obj(f, strip_space=True, fold_dict=True)

with open("output_with_libs.yml", "w") as outf:
  xmlplain.obj_to_yaml(root, outf)