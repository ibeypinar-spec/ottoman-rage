import unreal

pc_bp = unreal.load_asset("/Game/Blueprints/Player/BP_OttomanPlayerController")
pc_cdo = unreal.get_default_object(pc_bp.generated_class())

# Mouse tıklaması ile hareket için gerekli ayarlar
pc_cdo.set_editor_property("show_mouse_cursor", True)
pc_cdo.set_editor_property("enable_click_events", True)
pc_cdo.set_editor_property("enable_touch_events", False)
pc_cdo.set_editor_property("default_mouse_cursor", unreal.MouseCursor.DEFAULT)


unreal.EditorAssetLibrary.save_asset("/Game/Blueprints/Player/BP_OttomanPlayerController")
print("PlayerController ayarlandı: Mouse cursor ve click events aktif.")
