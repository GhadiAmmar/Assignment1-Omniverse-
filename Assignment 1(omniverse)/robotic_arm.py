from pxr import Usd, UsdGeom

stage = Usd.Stage.CreateNew("robot.usda")
xform = UsdGeom.Xform.Define(stage, "/Robot")
robot = UsdGeom.Xform.Define(stage, "/Robot")
stage.setDefaultPrim(robot.GetPrim())

def add_component(name, file_path, translate, rotate=(0, 0, 0), scale=(1, 1, 1)):
    xform = UsdGeom.Xform.Define(stage, f"/RoboticArm/{name}")
    UsdGeom.XformCommonAPI(xform).setTranslate(translate)
    UsdGeom.XformCommonAPI(xform).setRotate(rotate)
    UsdGeom.XformCommonAPI(xform).setScale(scale)
    xform.GetPrim().GetReferences().AddReference(file_path)

add_component("base", "base.usda", (0, 0, 0), rotate=(0, 0, 0), scale=(1, 1, 1))
add_component("lower_arm", "lower_arm.usda", (0, 0, 0), rotate=(0, 0, 0), scale=(1, 1, 1))
add_component("upper_arm", "upper_arm.usda", (0, 0, 0), rotate=(0, 0, 0), scale=(1, 1, 1))
add_component("gripper", "gripper.usda", (0, 0, 0), rotate=(0, 0, 0), scale=(1, 1, 1))
