import unreal

at = unreal.AssetToolsHelpers.get_asset_tools()
eal = unreal.EditorAssetLibrary

INPUT_DIR = "/Game/Input"
if not eal.does_directory_exist(INPUT_DIR):
    eal.make_directory(INPUT_DIR)

def make_input_action(name, value_type=unreal.InputActionValueType.BOOLEAN):
    path = f"{INPUT_DIR}/{name}"
    if eal.does_asset_exist(path):
        ia = unreal.load_asset(path)
    else:
        factory = unreal.InputAction_Factory()
        ia = at.create_asset(name, INPUT_DIR, unreal.InputAction, factory)
    ia.set_editor_property("value_type", value_type)
    eal.save_asset(path)
    return ia

# Aksiyonlar
ia_move   = make_input_action("IA_Move")     # sol tık ile hareket (bool)
ia_q      = make_input_action("IA_SkillQ")
ia_w      = make_input_action("IA_SkillW")
ia_e      = make_input_action("IA_SkillE")
ia_r      = make_input_action("IA_SkillR")
print("Input Action'lar olusturuldu.")

# Mapping Context
imc_path = f"{INPUT_DIR}/IMC_Ottoman"
if eal.does_asset_exist(imc_path):
    imc = unreal.load_asset(imc_path)
else:
    factory = unreal.InputMappingContext_Factory()
    imc = at.create_asset("IMC_Ottoman", INPUT_DIR, unreal.InputMappingContext, factory)

# Mevcut eşlemeleri temizle (idempotent olsun)
try:
    imc.set_editor_property("mappings", [])
except Exception:
    pass

# Tuş eşlemeleri - mappings dizisini doğrudan kur
def K(name):
    k = unreal.Key()
    k.set_editor_property("key_name", name)
    return k

def mapping(action, key_name):
    m = unreal.EnhancedActionKeyMapping()
    m.set_editor_property("action", action)
    m.set_editor_property("key", K(key_name))
    return m

mappings = [
    mapping(ia_move, "LeftMouseButton"),
    mapping(ia_q, "Q"),
    mapping(ia_w, "W"),
    mapping(ia_e, "E"),
    mapping(ia_r, "R"),
]
imc.set_editor_property("mappings", mappings)

eal.save_asset(imc_path)
print("IMC_Ottoman olusturuldu ve tuslar eslendi: SolTik=Move, Q/W/E/R=Skiller")
print("TAMAMLANDI")
