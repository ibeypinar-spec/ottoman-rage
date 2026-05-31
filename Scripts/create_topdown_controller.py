import unreal

# Mevcut controller'ı sil ve yeniden oluştur
asset_tools = unreal.AssetToolsHelpers.get_asset_tools()

# Önce mevcut varsa sil
if unreal.EditorAssetLibrary.does_asset_exist("/Game/Blueprints/Player/BP_OttomanPlayerController"):
    unreal.EditorAssetLibrary.delete_asset("/Game/Blueprints/Player/BP_OttomanPlayerController")
    print("Eski controller silindi.")

# UE'nin built-in APlayerController'dan türet
factory = unreal.BlueprintFactory()
factory.set_editor_property("parent_class", unreal.PlayerController)
new_pc = asset_tools.create_asset(
    "BP_OttomanPlayerController",
    "/Game/Blueprints/Player",
    None, factory
)

# CDO üzerinden mouse ayarları
cdo = unreal.get_default_object(new_pc.generated_class())
cdo.set_editor_property("show_mouse_cursor", True)
cdo.set_editor_property("enable_click_events", True)
cdo.set_editor_property("default_mouse_cursor", unreal.MouseCursor.DEFAULT)

# Event Graph'a manuel ekleme için not
print("""
Controller oluşturuldu!

Şimdi BP_OttomanPlayerController'ı açıp Event Graph'a şu node'ları ekleyin:
1. InputAction (mouse sol tık) → Get Hit Result Under Cursor by Channel → Simple Move to Location

NOT: AI Navigation için NavMesh Bounds Volume'u seviyeye eklemeyi unutmayın!
""")

unreal.BlueprintEditorLibrary.compile_blueprint(new_pc)
unreal.EditorAssetLibrary.save_asset("/Game/Blueprints/Player/BP_OttomanPlayerController")
