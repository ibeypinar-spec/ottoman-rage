import unreal

# Blueprint ve graph'ı al
pc_bp = unreal.load_asset("/Game/Blueprints/Player/BP_OttomanPlayerController")
graphs = unreal.BlueprintEditorLibrary.get_blueprint_event_graphs(pc_bp)
graph = graphs[0]  # EventGraph

# Mevcut devre dışı node'ları temizle
all_nodes = unreal.BlueprintEditorLibrary.get_graph_nodes(graph)
for node in all_nodes:
    unreal.BlueprintEditorLibrary.remove_graph_node(pc_bp, node)

# --- NODE'LARI OLUŞTUR ---

# 1. Event Tick
tick_node = unreal.BlueprintEditorLibrary.add_event_node(
    pc_bp, graph, "Event Tick"
)

# 2. Is Input Key Down
key_node = unreal.BlueprintEditorLibrary.add_function_node(
    pc_bp, graph,
    "/Script/Engine.PlayerController:IsInputKeyDown"
)

# 3. Get Hit Result Under Cursor by Channel
hit_node = unreal.BlueprintEditorLibrary.add_function_node(
    pc_bp, graph,
    "/Script/Engine.PlayerController:GetHitResultUnderCursorByChannel"
)

# 4. Break Hit Result
break_node = unreal.BlueprintEditorLibrary.add_function_node(
    pc_bp, graph,
    "/Script/Engine.KismetSystemLibrary:BreakHitResult"
)

# 5. Simple Move to Location
move_node = unreal.BlueprintEditorLibrary.add_function_node(
    pc_bp, graph,
    "/Script/AIModule.AIBlueprintHelperLibrary:SimpleMoveToLocation"
)

# 6. Get Player Controller (Self referansı için)
self_node = unreal.BlueprintEditorLibrary.add_function_node(
    pc_bp, graph,
    "/Script/Engine.GameplayStatics:GetPlayerController"
)

# --- BAĞLANTILARI YAP ---
# Tick -> Key Down
unreal.BlueprintEditorLibrary.connect_graph_pin(
    tick_node, "then",       # Event Tick exec out
    key_node, "execute"      # IsInputKeyDown exec in
)

# Key Down (true branch) -> Hit
unreal.BlueprintEditorLibrary.connect_graph_pin(
    key_node, "then",
    hit_node, "execute"
)

# Hit Result -> Break
hit_result_pin = unreal.BlueprintEditorLibrary.get_node_pin(hit_node, "Hit Result")
break_in_pin   = unreal.BlueprintEditorLibrary.get_node_pin(break_node, "Hit Result")
unreal.BlueprintEditorLibrary.connect_graph_pin(
    hit_node, "Hit Result",
    break_node, "Hit Result"
)

# Break Location -> Move to Location (Location pin)
unreal.BlueprintEditorLibrary.connect_graph_pin(
    break_node, "Location",
    move_node, "Dest"
)

# Self -> Move Controller pin
unreal.BlueprintEditorLibrary.connect_graph_pin(
    self_node, "Return Value",
    move_node, "Controller"
)

# --- NODE KONUMLARI ---
tick_node.node_pos_x  = 0;    tick_node.node_pos_y  = 0
key_node.node_pos_x   = 200;  key_node.node_pos_y   = 0
hit_node.node_pos_x   = 450;  hit_node.node_pos_y   = 0
break_node.node_pos_x = 700;  break_node.node_pos_y = 0
move_node.node_pos_x  = 950;  move_node.node_pos_y  = 0
self_node.node_pos_x  = 700;  self_node.node_pos_y  = 200

# Derle ve kaydet
unreal.BlueprintEditorLibrary.compile_blueprint(pc_bp)
unreal.EditorAssetLibrary.save_asset("/Game/Blueprints/Player/BP_OttomanPlayerController")
print("PlayerController Event Graph kuruldu ve derlendi!")
