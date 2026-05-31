import unreal

asset_tools = unreal.AssetToolsHelpers.get_asset_tools()

blueprints = [
    ("/Game/Blueprints/GameMode/BP_OttomanGameMode",   "GameModeBase"),
    ("/Game/Blueprints/Player/BP_OttomanPlayerController", "PlayerController"),
    ("/Game/Blueprints/Player/BP_OttomanCharacterBase", "Character"),
    ("/Game/Blueprints/Camera/BP_IsometricCamera",     "Actor"),
    ("/Game/Blueprints/Enemy/BP_EnemyBase",            "Character"),
]

for asset_path, parent_class_name in blueprints:
    package_path, asset_name = asset_path.rsplit("/", 1)
    parent_class = unreal.load_class(None, f"/Script/Engine.{parent_class_name}")
    factory = unreal.BlueprintFactory()
    factory.set_editor_property("parent_class", parent_class)
    asset = asset_tools.create_asset(asset_name, package_path, None, factory)
    if asset:
        print(f"OLUŞTURULDU: {asset_path}")
    else:
        print(f"HATA: {asset_path}")

unreal.EditorAssetLibrary.save_directory("/Game/Blueprints/", False, True)
print("Tüm Blueprint'ler kaydedildi.")
