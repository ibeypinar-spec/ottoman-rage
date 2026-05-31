import unreal

# BP_IsometricCamera Actor'unu konfigüre et
# Spring Arm + Camera component ekle (Python API component eklemeyi desteklemiyor,
# bu nedenle varsayılan değerleri CDO üzerinden ayarlıyoruz)

# BP_OttomanCharacterBase ayarları
char_bp = unreal.load_asset("/Game/Blueprints/Player/BP_OttomanCharacterBase")
char_cdo = unreal.get_default_object(char_bp.generated_class())

# Karakterin fizik ve hareket ayarları
movement = char_cdo.get_editor_property("character_movement")
if movement:
    movement.set_editor_property("max_walk_speed", 400.0)
    movement.set_editor_property("rotation_rate", unreal.Rotator(0, 540, 0))
    movement.set_editor_property("use_controller_desired_rotation", False)
    movement.set_editor_property("orient_rotation_to_movement", True)

# Karakterin rotasyonu kontrolcüye bağlı olmasın (izometrik için)
char_cdo.set_editor_property("use_controller_rotation_yaw", False)
char_cdo.set_editor_property("use_controller_rotation_pitch", False)
char_cdo.set_editor_property("use_controller_rotation_roll", False)

unreal.EditorAssetLibrary.save_asset("/Game/Blueprints/Player/BP_OttomanCharacterBase")
print("Karakter izometrik hareket ayarları yapıldı.")
