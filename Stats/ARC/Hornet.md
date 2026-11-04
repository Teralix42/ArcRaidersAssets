# Hornet

[ARC stats](README.md) · [Machine-readable data](arc_parts.json) · [Damage model](Damage_Model.md)

**Configured frame rule:** 200 HP. **Internal class:** `C_LightDrone_Elite`.

Frame HP is a balancing rule, not the sum of every limb or plate. Part rules and damage propagation are separate. `—` means unknown or unassigned.

[Interactive Blender inspection model](Models/Hornet.blend) · Native textures and inspector are packed into the file.

<a href="Renders/Hornet/01_Original_Materials_C.png"><img src="Renders/Hornet/01_Original_Materials_C.png" width="48%" alt="Hornet: Original Materials"></a>
<a href="Renders/Hornet/03_Part_Health_C.png"><img src="Renders/Hornet/03_Part_Health_C.png" width="48%" alt="Hornet: Part Health"></a>

### Layers and views

| Layer | Visible structure |
| --- | --- |
| A | Core + limb structure |
| B | Without armor |
| C | Full model |

<details>
<summary>All six views, including inner layers</summary>


**A: Core + limb structure**

<a href="Renders/Hornet/01_Original_Materials_A.png"><img src="Renders/Hornet/01_Original_Materials_A.png" width="32%" alt="Original Materials, layer A"></a>
<a href="Renders/Hornet/02_Part_Type_A.png"><img src="Renders/Hornet/02_Part_Type_A.png" width="32%" alt="Part Type, layer A"></a>
<a href="Renders/Hornet/03_Part_Health_A.png"><img src="Renders/Hornet/03_Part_Health_A.png" width="32%" alt="Part Health, layer A"></a>
<a href="Renders/Hornet/04_Break_Off_A.png"><img src="Renders/Hornet/04_Break_Off_A.png" width="32%" alt="Break Off, layer A"></a>
<a href="Renders/Hornet/05_Scavenge_Interaction_A.png"><img src="Renders/Hornet/05_Scavenge_Interaction_A.png" width="32%" alt="Scavenge Interaction, layer A"></a>
<a href="Renders/Hornet/06_Damage_Targets_A.png"><img src="Renders/Hornet/06_Damage_Targets_A.png" width="32%" alt="Damage Targets, layer A"></a>

**B: Without armor**

<a href="Renders/Hornet/01_Original_Materials_B.png"><img src="Renders/Hornet/01_Original_Materials_B.png" width="32%" alt="Original Materials, layer B"></a>
<a href="Renders/Hornet/02_Part_Type_B.png"><img src="Renders/Hornet/02_Part_Type_B.png" width="32%" alt="Part Type, layer B"></a>
<a href="Renders/Hornet/03_Part_Health_B.png"><img src="Renders/Hornet/03_Part_Health_B.png" width="32%" alt="Part Health, layer B"></a>
<a href="Renders/Hornet/04_Break_Off_B.png"><img src="Renders/Hornet/04_Break_Off_B.png" width="32%" alt="Break Off, layer B"></a>
<a href="Renders/Hornet/05_Scavenge_Interaction_B.png"><img src="Renders/Hornet/05_Scavenge_Interaction_B.png" width="32%" alt="Scavenge Interaction, layer B"></a>
<a href="Renders/Hornet/06_Damage_Targets_B.png"><img src="Renders/Hornet/06_Damage_Targets_B.png" width="32%" alt="Damage Targets, layer B"></a>

**C: Full model**

<a href="Renders/Hornet/01_Original_Materials_C.png"><img src="Renders/Hornet/01_Original_Materials_C.png" width="32%" alt="Original Materials, layer C"></a>
<a href="Renders/Hornet/02_Part_Type_C.png"><img src="Renders/Hornet/02_Part_Type_C.png" width="32%" alt="Part Type, layer C"></a>
<a href="Renders/Hornet/03_Part_Health_C.png"><img src="Renders/Hornet/03_Part_Health_C.png" width="32%" alt="Part Health, layer C"></a>
<a href="Renders/Hornet/04_Break_Off_C.png"><img src="Renders/Hornet/04_Break_Off_C.png" width="32%" alt="Break Off, layer C"></a>
<a href="Renders/Hornet/05_Scavenge_Interaction_C.png"><img src="Renders/Hornet/05_Scavenge_Interaction_C.png" width="32%" alt="Scavenge Interaction, layer C"></a>
<a href="Renders/Hornet/06_Damage_Targets_C.png"><img src="Renders/Hornet/06_Damage_Targets_C.png" width="32%" alt="Damage Targets, layer C"></a>

</details>

### Weak and critical parts

| Part | Configured HP | Group | Baseline physical damage × |
| --- | --- | --- | --- |
| Core_01 | 1300 | Critical | 1.5 |

### Every named part

These records also include sockets, bones, and proxy components; they are not all independent damageable hitboxes. The weapon’s separate ARC armor and weak-point multipliers still apply where indicated in JSON.

| Part | Configured HP | Resistance group | Physical damage × | Health rules |
| --- | --- | --- | --- | --- |
| Thruster_L_01_Socket | — | — | — |  |
| Thruster_R_01_Socket | — | — | — |  |
| Thruster_R_02_Socket | — | — | — |  |
| Thruster_L_02_Socket | — | — | — |  |
| Eye_Socket | — | — | — |  |
| Barrel_Socket | — | — | — |  |
| Frame_01 | 200 | Normal | 1 | 5 |
| Core_01 | 1300 | Critical | 1.5 | 4 |
| Head_01 | 1300 | Fragile | 1.2 | 4 |
| HornetShield_01 | 48 | Armor | 0.4 | 0 |
| HornetShield_Lower_01 | 48 | Armor | 0.4 | 0 |
| HornetHatch_L_01 | 6 | Armor | 0.4 | 2 |
| HornetHatch_R_01 | 6 | Armor | 0.4 | 2 |
| HornetWeaponAttachment | 1000 | Sturdy | 0.4 | 3 |
| weapon_Hornet_01 | 1000 | Sturdy | 0.4 | 7 |
| Thruster_L_01 | 30 | Fragile | 1.2 | 6 |
| HornetThrusterShield_L_01 | 16 | Armor | 0.4 | 1 |
| Thruster_L_02 | 30 | Fragile | 1.2 | 6 |
| Thruster_R_01 | 30 | Fragile | 1.2 | 6 |
| HornetThrusterShield_R_01 | 16 | Armor | 0.4 | 1 |
| Thruster_R_02 | 30 | Fragile | 1.2 | 6 |
| EyeDummyPart | — | — | — |  |

### Exact health assignment rules

| Rule | Tag query | HP | Matched parts |
| --- | --- | --- | --- |
| 0 | ID.Armor.Heavy | 48 | HornetShield_01, HornetShield_Lower_01 |
| 1 | ID.Armor.Medium | 16 | HornetThrusterShield_L_01, HornetThrusterShield_R_01 |
| 2 | ID.Armor.Light | 6 | HornetHatch_L_01, HornetHatch_R_01 |
| 3 | ALL(Group.Indestructible, NONE(ID.Weapon.Rifle)) | 1000 | HornetWeaponAttachment |
| 4 | Group.Critical | 1300 | Core_01, Head_01 |
| 5 | ID.Frame | 200 | Frame_01 |
| 6 | ID.Thruster | 30 | Thruster_L_01, Thruster_L_02, Thruster_R_01, Thruster_R_02 |
| 7 | ID.Weapon.Rifle | 1000 | weapon_Hornet_01 |

Some actor/style sources have partial-decoding warnings; the balancing health tables parsed separately. The JSON retains the warnings and recovered destruction settings.

<details>
<summary>Actual game source files</summary>

- [Content/Pioneer/Enemies/EliteDrone/Hornet/CS_LightDrone_Elite_SK.json](../Sources/PioneerGame/Content/Pioneer/Enemies/EliteDrone/Hornet/CS_LightDrone_Elite_SK.json)
- [Content/Pioneer/Enemies/EliteDrone/Hornet/C_LightDrone_Elite.json](../Sources/PioneerGame/Content/Pioneer/Enemies/EliteDrone/Hornet/C_LightDrone_Elite.json)
- [Content/Pioneer/Enemies/EliteDrone/Hornet/DataAssets/CSSC_LightDroneElite.json](../Sources/PioneerGame/Content/Pioneer/Enemies/EliteDrone/Hornet/DataAssets/CSSC_LightDroneElite.json)
- [Content/Pioneer/Enemies/EliteDrone/Hornet/DataAssets/DA_Balancing_C_LightDrone_Elite.json](../Sources/PioneerGame/Content/Pioneer/Enemies/EliteDrone/Hornet/DataAssets/DA_Balancing_C_LightDrone_Elite.json)
- [Content/Pioneer/Enemies/EliteDrone/Hornet/DataAssets/DA_EnemyMetaData_LightDroneElite.json](../Sources/PioneerGame/Content/Pioneer/Enemies/EliteDrone/Hornet/DataAssets/DA_EnemyMetaData_LightDroneElite.json)
- [Content/Pioneer/Enemies/EliteDrone/Hornet/DataAssets/DA_EnemyType_LightDroneElite.json](../Sources/PioneerGame/Content/Pioneer/Enemies/EliteDrone/Hornet/DataAssets/DA_EnemyType_LightDroneElite.json)

</details>
