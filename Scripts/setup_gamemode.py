import unreal

# GameMode'a PlayerController ve Character ata
gm = unreal.load_asset("/Game/Blueprints/GameMode/BP_OttomanGameMode")
pc = unreal.load_class(None, "/Game/Blueprints/Player/BP_OttomanPlayerController.BP_OttomanPlayerController_C")
ch = unreal.load_class(None, "/Game/Blueprints/Player/BP_OttomanCharacterBase.BP_OttomanCharacterBase_C")

gm_cdo = unreal.get_default_object(gm.generated_class())
gm_cdo.set_editor_property("player_controller_class", pc)
gm_cdo.set_editor_property("default_pawn_class", ch)

unreal.EditorAssetLibrary.save_asset("/Game/Blueprints/GameMode/BP_OttomanGameMode")
print("GameMode ayarlandı: PlayerController ve Character atandı.")
