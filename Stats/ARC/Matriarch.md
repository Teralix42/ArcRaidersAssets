# Matriarch

[ARC stats](README.md) · [Damage model](Damage_Model.md)

**Configured frame rule:** 23100 HP. **Internal class:** `C_Spearmint`.

Frame HP is assigned separately from part HP. A dash marks an unknown or unassigned value.

[Balancing and part HP](../Sources/PioneerGame/Content/Pioneer/Enemies/MintType/Spearmint/DataAssets/DA_Balancing_C_Spearmint.json) · [Enemy type](../Sources/PioneerGame/Content/Pioneer/Enemies/MintType/Spearmint/DataAssets/DA_EnemyType_Spearmint.json)

<details>
<summary>More game files</summary>

- [CS_Spearmint.json](../Sources/PioneerGame/Content/Pioneer/Enemies/MintType/Spearmint/CS_Spearmint.json)
- [C_Spearmint.json](../Sources/PioneerGame/Content/Pioneer/Enemies/MintType/Spearmint/C_Spearmint.json)
- [CSSC_Spearmint.json](../Sources/PioneerGame/Content/Pioneer/Enemies/MintType/Spearmint/DataAssets/CSSC_Spearmint.json)
- [DA_EnemyMetaData_Spearmint.json](../Sources/PioneerGame/Content/Pioneer/Enemies/MintType/Spearmint/DataAssets/DA_EnemyMetaData_Spearmint.json)

</details>

[Interactive Blender inspection model](Models/Matriarch.blend) · Native textures and inspector are packed into the file.

<a href="Renders/Matriarch/01_Original_Materials_C.png"><img src="Renders/Matriarch/01_Original_Materials_C.png" width="48%" alt="Matriarch: Original Materials"></a>
<a href="Renders/Matriarch/03_Part_Health_C.png"><img src="Renders/Matriarch/03_Part_Health_C.png" width="48%" alt="Matriarch: Part Health"></a>

<details>
<summary>All stat renders</summary>

**Original materials**

<p align="center">
  <a href="Renders/Matriarch/01_Original_Materials_A.png"><img src="Renders/Matriarch/01_Original_Materials_A.png" width="31%" alt="Matriarch original materials"></a>
  <a href="Renders/Matriarch/01_Original_Materials_B.png"><img src="Renders/Matriarch/01_Original_Materials_B.png" width="31%" alt="Matriarch original materials"></a>
  <a href="Renders/Matriarch/01_Original_Materials_C.png"><img src="Renders/Matriarch/01_Original_Materials_C.png" width="31%" alt="Matriarch original materials"></a>
</p>

**Part type**

<p align="center">
  <a href="Renders/Matriarch/02_Part_Type_A.png"><img src="Renders/Matriarch/02_Part_Type_A.png" width="31%" alt="Matriarch part type"></a>
  <a href="Renders/Matriarch/02_Part_Type_B.png"><img src="Renders/Matriarch/02_Part_Type_B.png" width="31%" alt="Matriarch part type"></a>
  <a href="Renders/Matriarch/02_Part_Type_C.png"><img src="Renders/Matriarch/02_Part_Type_C.png" width="31%" alt="Matriarch part type"></a>
</p>

**Part health**

<p align="center">
  <a href="Renders/Matriarch/03_Part_Health_A.png"><img src="Renders/Matriarch/03_Part_Health_A.png" width="31%" alt="Matriarch part health"></a>
  <a href="Renders/Matriarch/03_Part_Health_B.png"><img src="Renders/Matriarch/03_Part_Health_B.png" width="31%" alt="Matriarch part health"></a>
  <a href="Renders/Matriarch/03_Part_Health_C.png"><img src="Renders/Matriarch/03_Part_Health_C.png" width="31%" alt="Matriarch part health"></a>
</p>

**Break-off parts**

<p align="center">
  <a href="Renders/Matriarch/04_Break_Off_A.png"><img src="Renders/Matriarch/04_Break_Off_A.png" width="31%" alt="Matriarch break-off parts"></a>
  <a href="Renders/Matriarch/04_Break_Off_B.png"><img src="Renders/Matriarch/04_Break_Off_B.png" width="31%" alt="Matriarch break-off parts"></a>
  <a href="Renders/Matriarch/04_Break_Off_C.png"><img src="Renders/Matriarch/04_Break_Off_C.png" width="31%" alt="Matriarch break-off parts"></a>
</p>

**Scavenging**

<p align="center">
  <a href="Renders/Matriarch/05_Scavenge_Interaction_A.png"><img src="Renders/Matriarch/05_Scavenge_Interaction_A.png" width="31%" alt="Matriarch scavenging"></a>
  <a href="Renders/Matriarch/05_Scavenge_Interaction_B.png"><img src="Renders/Matriarch/05_Scavenge_Interaction_B.png" width="31%" alt="Matriarch scavenging"></a>
  <a href="Renders/Matriarch/05_Scavenge_Interaction_C.png"><img src="Renders/Matriarch/05_Scavenge_Interaction_C.png" width="31%" alt="Matriarch scavenging"></a>
</p>

**Damage targets**

<p align="center">
  <a href="Renders/Matriarch/06_Damage_Targets_A.png"><img src="Renders/Matriarch/06_Damage_Targets_A.png" width="31%" alt="Matriarch damage targets"></a>
  <a href="Renders/Matriarch/06_Damage_Targets_B.png"><img src="Renders/Matriarch/06_Damage_Targets_B.png" width="31%" alt="Matriarch damage targets"></a>
  <a href="Renders/Matriarch/06_Damage_Targets_C.png"><img src="Renders/Matriarch/06_Damage_Targets_C.png" width="31%" alt="Matriarch damage targets"></a>
</p>

</details>

### Weak and critical parts

| Part | Configured HP | Group | Baseline physical damage × |
| --- | --- | --- | --- |
| Core_01 | 30000 | Critical | 1.5 |
| LowerLeg_01_Weakpoint_01_L_01 | 6000 | WeakPoint | 1.5 |
| LowerLeg_01_Weakpoint_01_L_02 | 6000 | WeakPoint | 1.5 |
| LowerLeg_01_Weakpoint_01_L_03 | 6000 | WeakPoint | 1.5 |
| LowerLeg_01_Weakpoint_01_R_01 | 6000 | WeakPoint | 1.5 |
| LowerLeg_01_Weakpoint_01_R_02 | 6000 | WeakPoint | 1.5 |
| LowerLeg_01_Weakpoint_01_R_03 | 6000 | WeakPoint | 1.5 |

### Outgoing damage rules

Configured values keyed by the part or attack tag. Attack timing and the final damage against a Raider depend on the attack and target.

| Tag | Damage type | Configured damage |
| --- | --- | --- |
| ID.Weapon.Blast | Explosive | 100 |

### Every named part

This list includes mesh records such as sockets and proxies. See the [damage model](Damage_Model.md) for how weapon multipliers apply to each resistance group.

| Part | Configured HP | Resistance group | Physical damage × | Health rules |
| --- | --- | --- | --- | --- |
| FootGroundContact_01_L_01 | 440 | — | — | 10 |
| FootGroundContact_01_L_02 | 440 | — | — | 10 |
| FootGroundContact_01_L_03 | 440 | — | — | 10 |
| FootGroundContact_01_R_01 | 440 | — | — | 10 |
| FootGroundContact_01_R_02 | 440 | — | — | 10 |
| FootGroundContact_01_R_03 | 440 | — | — | 10 |
| UpperLegGroundContact_01_L_01 | — | — | — |  |
| LowerLegGroundContact_01_L_01 | — | — | — |  |
| UpperLegGroundContact_01_L_02 | — | — | — |  |
| LowerLegGroundContact_01_L_02 | — | — | — |  |
| UpperLegGroundContact_01_L_03 | — | — | — |  |
| LowerLegGroundContact_01_L_03 | — | — | — |  |
| UpperLegGroundContact_01_R_01 | — | — | — |  |
| LowerLegGroundContact_01_R_01 | — | — | — |  |
| UpperLegGroundContact_01_R_02 | — | — | — |  |
| LowerLegGroundContact_01_R_02 | — | — | — |  |
| UpperLegGroundContact_01_R_03 | — | — | — |  |
| LowerLegGroundContact_01_R_03 | — | — | — |  |
| Weapon_Launcher_Socket | 150000 | — | — | 9 |
| Head_Dispenser_4 | — | — | — |  |
| Head_Dispenser_3 | — | — | — |  |
| Head_Dispenser_2 | — | — | — |  |
| Head_Dispenser_1 | — | — | — |  |
| Body_01 | 23100 | Normal | 1 | 0 |
| Head_01 | 30000 | Normal | 1 | 2 |
| Core_01 | 30000 | Critical | 1.5 | 3 |
| Eye_01 | 150000 | Normal | 1 | 9 |
| Head_01_Armor_01_L_01 | 300 | Armor | 0.4 | 8 |
| Head_01_Armor_01_R_01 | 300 | Armor | 0.4 | 8 |
| Head_01_Armor_02_L_01 | 300 | Armor | 0.4 | 8 |
| Head_01_Armor_02_R_01 | 300 | Armor | 0.4 | 8 |
| Head_01_Armor_03_L_01 | 300 | Armor | 0.4 | 8 |
| Head_01_Armor_03_R_01 | 300 | Armor | 0.4 | 8 |
| Head_01_Armor_04_L_01 | 300 | Armor | 0.4 | 8 |
| Head_01_Armor_04_R_01 | 300 | Armor | 0.4 | 8 |
| Head_01_Armor_06_C_01 | 150000 | Armor | 0.4 | 9 |
| Head_01_Armor_07_L_01 | 300 | Armor | 0.4 | 8 |
| Head_01_Armor_07_R_01 | 300 | Armor | 0.4 | 8 |
| Head_01_Armor_08_L_01 | 300 | Armor | 0.4 | 8 |
| Head_01_Armor_08_R_01 | 300 | Armor | 0.4 | 8 |
| Head_01_Armor_10_L_01 | 300 | Armor | 0.4 | 8 |
| Head_01_Armor_10_R_01 | 300 | Armor | 0.4 | 8 |
| Head_01_Armor_L_09 | 300 | Armor | 0.4 | 8 |
| Head_01_HatchFrame_C_01 | 100000 | Normal | 1 | 12 |
| Head_01_Insides_01_L_01 | 5250 | Fragile | 1.2 | 5 |
| Head_01_Insides_01_R_01 | 5250 | Fragile | 1.2 | 5 |
| Head_01_Insides_02_L_01 | 5250 | Fragile | 1.2 | 5 |
| Head_01_Insides_02_R_01 | 5250 | Fragile | 1.2 | 5 |
| Head_01_Insides_03_L_01 | 5250 | Fragile | 1.2 | 5 |
| Head_01_Insides_03_R_01 | 5250 | Fragile | 1.2 | 5 |
| Head_01_Insides_04_L_01 | 5250 | Fragile | 1.2 | 5 |
| Head_01_Insides_04_R_01 | 5250 | Fragile | 1.2 | 5 |
| Weapon_Launcher_01 | 150000 | Sturdy | 0.4 | 9 |
| UpperLeg_01_L_01 | 4050 | Normal | 1 | 1 |
| Hydraulics_UpperLeg_01_L_01 | 30000 | Normal | 1 | 7 |
| LowerLeg_01_L_01 | 4050 | Normal | 1 | 1 |
| Ankle_01_L_01 | 440 | Normal | 1 | 10 |
| Foot_01_L_01 | 440 | Normal | 1 | 10 |
| Hydraulics_Foot_01_L_01 | 30000 | Normal | 1 | 7 |
| Hydraulics_UpperLeg_02_L_01 | 30000 | Normal | 1 | 7 |
| LowerLeg_01_Armor_01_L_01 | 300 | Armor | 0.4 | 8 |
| LowerLeg_01_Insides_01_L_01 | 1500 | Fragile | 1.2 | 6 |
| LowerLeg_01_Weakpoint_01_L_01 | 6000 | WeakPoint | 1.5 | 4 |
| UpperLeg_01_Armor_01_L_01 | 300 | Armor | 0.4 | 8 |
| UpperLeg_01_L_02 | 4050 | Normal | 1 | 1 |
| Hydraulics_UpperLeg_01_L_02 | 30000 | Normal | 1 | 7 |
| LowerLeg_01_L_02 | 4050 | Normal | 1 | 1 |
| Ankle_01_L_02 | 440 | Normal | 1 | 10 |
| Foot_01_L_02 | 440 | Normal | 1 | 10 |
| Hydraulics_Foot_01_L_02 | 30000 | Normal | 1 | 7 |
| Hydraulics_UpperLeg_02_L_02 | 30000 | Normal | 1 | 7 |
| LowerLeg_01_Armor_01_L_02 | 300 | Armor | 0.4 | 8 |
| LowerLeg_01_Insides_01_L_02 | 1500 | Fragile | 1.2 | 6 |
| LowerLeg_01_Weakpoint_01_L_02 | 6000 | WeakPoint | 1.5 | 4 |
| UpperLeg_01_Armor_01_L_02 | 300 | Armor | 0.4 | 8 |
| UpperLeg_01_L_03 | 4050 | Normal | 1 | 1 |
| Hydraulics_UpperLeg_01_L_03 | 30000 | Normal | 1 | 7 |
| LowerLeg_01_L_03 | 4050 | Normal | 1 | 1 |
| Ankle_01_L_03 | 440 | Normal | 1 | 10 |
| Foot_01_L_03 | 440 | Normal | 1 | 10 |
| Hydraulics_Foot_01_L_03 | 30000 | Normal | 1 | 7 |
| Hydraulics_UpperLeg_02_L_03 | 30000 | Normal | 1 | 7 |
| LowerLeg_01_Armor_01_L_03 | 300 | Armor | 0.4 | 8 |
| LowerLeg_01_Insides_01_L_03 | 1500 | Fragile | 1.2 | 6 |
| LowerLeg_01_Weakpoint_01_L_03 | 6000 | WeakPoint | 1.5 | 4 |
| UpperLeg_01_Armor_01_L_03 | 300 | Armor | 0.4 | 8 |
| UpperLeg_01_R_01 | 4050 | Normal | 1 | 1 |
| Hydraulics_UpperLeg_01_R_01 | 30000 | Normal | 1 | 7 |
| LowerLeg_01_R_01 | 4050 | Normal | 1 | 1 |
| Ankle_01_R_01 | 440 | Normal | 1 | 10 |
| Foot_01_R_01 | 440 | Normal | 1 | 10 |
| Hydraulics_Foot_01_R_01 | 30000 | Normal | 1 | 7 |
| Hydraulics_UpperLeg_02_R_01 | 30000 | Normal | 1 | 7 |
| LowerLeg_01_Armor_01_R_01 | 300 | Armor | 0.4 | 8 |
| LowerLeg_01_Insides_01_R_01 | 1500 | Fragile | 1.2 | 6 |
| LowerLeg_01_Weakpoint_01_R_01 | 6000 | WeakPoint | 1.5 | 4 |
| UpperLeg_01_Armor_01_R_01 | 300 | Armor | 0.4 | 8 |
| UpperLeg_01_R_02 | 4050 | Normal | 1 | 1 |
| Hydraulics_UpperLeg_01_R_02 | 30000 | Normal | 1 | 7 |
| LowerLeg_01_R_02 | 4050 | Normal | 1 | 1 |
| Ankle_01_R_02 | 440 | Normal | 1 | 10 |
| Foot_01_R_02 | 440 | Normal | 1 | 10 |
| Hydraulics_Foot_01_R_02 | 30000 | Normal | 1 | 7 |
| Hydraulics_UpperLeg_02_R_02 | 30000 | Normal | 1 | 7 |
| LowerLeg_01_Armor_01_R_02 | 300 | Armor | 0.4 | 8 |
| LowerLeg_01_Insides_01_R_02 | 1500 | Fragile | 1.2 | 6 |
| LowerLeg_01_Weakpoint_01_R_02 | 6000 | WeakPoint | 1.5 | 4 |
| UpperLeg_01_Armor_01_R_02 | 300 | Armor | 0.4 | 8 |
| UpperLeg_01_R_03 | 4050 | Normal | 1 | 1 |
| Hydraulics_UpperLeg_01_R_03 | 30000 | Normal | 1 | 7 |
| LowerLeg_01_R_03 | 4050 | Normal | 1 | 1 |
| Ankle_01_R_03 | 440 | Normal | 1 | 10 |
| Foot_01_R_03 | 440 | Normal | 1 | 10 |
| Hydraulics_Foot_01_R_03 | 30000 | Normal | 1 | 7 |
| Hydraulics_UpperLeg_02_R_03 | 30000 | Normal | 1 | 7 |
| LowerLeg_01_Armor_01_R_03 | 300 | Armor | 0.4 | 8 |
| LowerLeg_01_Insides_01_R_03 | 1500 | Fragile | 1.2 | 6 |
| LowerLeg_01_Weakpoint_01_R_03 | 6000 | WeakPoint | 1.5 | 4 |
| UpperLeg_01_Armor_01_R_03 | 300 | Armor | 0.4 | 8 |
| EyeStaticMeshDummy | — | — | — |  |
| ForProto | 23100 | — | — | 11 |
| Grenade | 23100 | — | — | 11 |
| VisionConeDummy | — | — | — |  |

### Exact health assignment rules

| Rule | Tag query | HP | Matched parts |
| --- | --- | --- | --- |
| 0 | ID.Frame | 23100 | Body_01 |
| 1 | ALL(ID.Leg, NONE(Group.Weakpoint)) | 4050 | UpperLeg_01_L_01, LowerLeg_01_L_01, UpperLeg_01_L_02, LowerLeg_01_L_02, UpperLeg_01_L_03, LowerLeg_01_L_03, UpperLeg_01_R_01, LowerLeg_01_R_01, UpperLeg_01_R_02, LowerLeg_01_R_02, UpperLeg_01_R_03, LowerLeg_01_R_03 |
| 2 | ID.Head | 30000 | Head_01 |
| 3 | ANY(ID.Core) | 30000 | Core_01 |
| 4 | ANY(Group.Weakpoint) | 6000 | LowerLeg_01_Weakpoint_01_L_01, LowerLeg_01_Weakpoint_01_L_02, LowerLeg_01_Weakpoint_01_L_03, LowerLeg_01_Weakpoint_01_R_01, LowerLeg_01_Weakpoint_01_R_02, LowerLeg_01_Weakpoint_01_R_03 |
| 5 | HealthGroup.Base | 5250 | Head_01_Insides_01_L_01, Head_01_Insides_01_R_01, Head_01_Insides_02_L_01, Head_01_Insides_02_R_01, Head_01_Insides_03_L_01, Head_01_Insides_03_R_01, Head_01_Insides_04_L_01, Head_01_Insides_04_R_01 |
| 6 | HealthGroup.Legs | 1500 | LowerLeg_01_Insides_01_L_01, LowerLeg_01_Insides_01_L_02, LowerLeg_01_Insides_01_L_03, LowerLeg_01_Insides_01_R_01, LowerLeg_01_Insides_01_R_02, LowerLeg_01_Insides_01_R_03 |
| 7 | HealthGroup.SubParts | 30000 | Hydraulics_UpperLeg_01_L_01, Hydraulics_Foot_01_L_01, Hydraulics_UpperLeg_02_L_01, Hydraulics_UpperLeg_01_L_02, Hydraulics_Foot_01_L_02, Hydraulics_UpperLeg_02_L_02, Hydraulics_UpperLeg_01_L_03, Hydraulics_Foot_01_L_03, Hydraulics_UpperLeg_02_L_03, Hydraulics_UpperLeg_01_R_01, Hydraulics_Foot_01_R_01, Hydraulics_UpperLeg_02_R_01, Hydraulics_UpperLeg_01_R_02, Hydraulics_Foot_01_R_02, Hydraulics_UpperLeg_02_R_02, Hydraulics_UpperLeg_01_R_03, Hydraulics_Foot_01_R_03, Hydraulics_UpperLeg_02_R_03 |
| 8 | ANY(ID.Armor) | 300 | Head_01_Armor_01_L_01, Head_01_Armor_01_R_01, Head_01_Armor_02_L_01, Head_01_Armor_02_R_01, Head_01_Armor_03_L_01, Head_01_Armor_03_R_01, Head_01_Armor_04_L_01, Head_01_Armor_04_R_01, Head_01_Armor_07_L_01, Head_01_Armor_07_R_01, Head_01_Armor_08_L_01, Head_01_Armor_08_R_01, Head_01_Armor_10_L_01, Head_01_Armor_10_R_01, Head_01_Armor_L_09, LowerLeg_01_Armor_01_L_01, UpperLeg_01_Armor_01_L_01, LowerLeg_01_Armor_01_L_02, UpperLeg_01_Armor_01_L_02, LowerLeg_01_Armor_01_L_03, UpperLeg_01_Armor_01_L_03, LowerLeg_01_Armor_01_R_01, UpperLeg_01_Armor_01_R_01, LowerLeg_01_Armor_01_R_02, UpperLeg_01_Armor_01_R_02, LowerLeg_01_Armor_01_R_03, UpperLeg_01_Armor_01_R_03 |
| 9 | Part.HealthGroup.Indestructable | 150000 | Weapon_Launcher_Socket, Eye_01, Head_01_Armor_06_C_01, Weapon_Launcher_01 |
| 10 | ANY(ID.Foot, ID.Ankle) | 440 | FootGroundContact_01_L_01, FootGroundContact_01_L_02, FootGroundContact_01_L_03, FootGroundContact_01_R_01, FootGroundContact_01_R_02, FootGroundContact_01_R_03, Ankle_01_L_01, Foot_01_L_01, Ankle_01_L_02, Foot_01_L_02, Ankle_01_L_03, Foot_01_L_03, Ankle_01_R_01, Foot_01_R_01, Ankle_01_R_02, Foot_01_R_02, Ankle_01_R_03, Foot_01_R_03 |
| 11 | ANY(ID.Weapon) | 23100 | ForProto, Grenade |
| 12 | ANY(ID.HatchFrame) | 100000 | Head_01_HatchFrame_C_01 |

<details>
<summary>Destruction and stun rules</summary>

**Destruction groups**

| Part query | Destruction damage | Max level | Game file |
| --- | --- | --- | --- |
| ID.Leg | 10000 | 1 | [Actor config](../Sources/PioneerGame/Content/Pioneer/Enemies/MintType/Spearmint/C_Spearmint.json) |
| ID.Head | 10000 | 1 | [Actor config](../Sources/PioneerGame/Content/Pioneer/Enemies/MintType/Spearmint/C_Spearmint.json) |

</details>
