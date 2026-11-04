# Firefly

[ARC stats](README.md) · [Machine-readable data](arc_parts.json) · [Damage model](Damage_Model.md)

**Configured frame rule:** 200 HP. **Internal class:** `C_EliteDrone_Flamethrower`.

Frame HP is a balancing rule, not the sum of every limb or plate. Part rules and damage propagation are separate. `—` means unknown or unassigned.

[Interactive Blender inspection model](Models/Firefly.blend) · Native textures and inspector are packed into the file.

<a href="Renders/Firefly/01_Original_Materials_C.png"><img src="Renders/Firefly/01_Original_Materials_C.png" width="48%" alt="Firefly: Original Materials"></a>
<a href="Renders/Firefly/03_Part_Health_C.png"><img src="Renders/Firefly/03_Part_Health_C.png" width="48%" alt="Firefly: Part Health"></a>

### Layers and views

| Layer | Visible structure |
| --- | --- |
| A | Core + limb structure |
| B | Without armor |
| C | Full model |

<details>
<summary>All six views, including inner layers</summary>


**A: Core + limb structure**

<a href="Renders/Firefly/01_Original_Materials_A.png"><img src="Renders/Firefly/01_Original_Materials_A.png" width="32%" alt="Original Materials, layer A"></a>
<a href="Renders/Firefly/02_Part_Type_A.png"><img src="Renders/Firefly/02_Part_Type_A.png" width="32%" alt="Part Type, layer A"></a>
<a href="Renders/Firefly/03_Part_Health_A.png"><img src="Renders/Firefly/03_Part_Health_A.png" width="32%" alt="Part Health, layer A"></a>
<a href="Renders/Firefly/04_Break_Off_A.png"><img src="Renders/Firefly/04_Break_Off_A.png" width="32%" alt="Break Off, layer A"></a>
<a href="Renders/Firefly/05_Scavenge_Interaction_A.png"><img src="Renders/Firefly/05_Scavenge_Interaction_A.png" width="32%" alt="Scavenge Interaction, layer A"></a>
<a href="Renders/Firefly/06_Damage_Targets_A.png"><img src="Renders/Firefly/06_Damage_Targets_A.png" width="32%" alt="Damage Targets, layer A"></a>

**B: Without armor**

<a href="Renders/Firefly/01_Original_Materials_B.png"><img src="Renders/Firefly/01_Original_Materials_B.png" width="32%" alt="Original Materials, layer B"></a>
<a href="Renders/Firefly/02_Part_Type_B.png"><img src="Renders/Firefly/02_Part_Type_B.png" width="32%" alt="Part Type, layer B"></a>
<a href="Renders/Firefly/03_Part_Health_B.png"><img src="Renders/Firefly/03_Part_Health_B.png" width="32%" alt="Part Health, layer B"></a>
<a href="Renders/Firefly/04_Break_Off_B.png"><img src="Renders/Firefly/04_Break_Off_B.png" width="32%" alt="Break Off, layer B"></a>
<a href="Renders/Firefly/05_Scavenge_Interaction_B.png"><img src="Renders/Firefly/05_Scavenge_Interaction_B.png" width="32%" alt="Scavenge Interaction, layer B"></a>
<a href="Renders/Firefly/06_Damage_Targets_B.png"><img src="Renders/Firefly/06_Damage_Targets_B.png" width="32%" alt="Damage Targets, layer B"></a>

**C: Full model**

<a href="Renders/Firefly/01_Original_Materials_C.png"><img src="Renders/Firefly/01_Original_Materials_C.png" width="32%" alt="Original Materials, layer C"></a>
<a href="Renders/Firefly/02_Part_Type_C.png"><img src="Renders/Firefly/02_Part_Type_C.png" width="32%" alt="Part Type, layer C"></a>
<a href="Renders/Firefly/03_Part_Health_C.png"><img src="Renders/Firefly/03_Part_Health_C.png" width="32%" alt="Part Health, layer C"></a>
<a href="Renders/Firefly/04_Break_Off_C.png"><img src="Renders/Firefly/04_Break_Off_C.png" width="32%" alt="Break Off, layer C"></a>
<a href="Renders/Firefly/05_Scavenge_Interaction_C.png"><img src="Renders/Firefly/05_Scavenge_Interaction_C.png" width="32%" alt="Scavenge Interaction, layer C"></a>
<a href="Renders/Firefly/06_Damage_Targets_C.png"><img src="Renders/Firefly/06_Damage_Targets_C.png" width="32%" alt="Damage Targets, layer C"></a>

</details>

### Weak and critical parts

| Part | Configured HP | Group | Baseline physical damage × |
| --- | --- | --- | --- |
| Core | 167 | Critical | 1.5 |

### Every named part

These records also include sockets, bones, and proxy components; they are not all independent damageable hitboxes. The weapon’s separate ARC armor and weak-point multipliers still apply where indicated in JSON.

| Part | Configured HP | Resistance group | Physical damage × | Health rules |
| --- | --- | --- | --- | --- |
| Barrel_Socket | — | — | — |  |
| Eye_Socket | — | — | — |  |
| Thruster_L_01_Socket | — | — | — |  |
| Thruster_L_02_Socket | — | — | — |  |
| Thruster_R_01_Socket | — | — | — |  |
| Thruster_R_02_Socket | — | — | — |  |
| Frame | 200 | Normal | 1 | 6 |
| Head | 1300 | Fragile | 1.2 | 5 |
| ShieldLower_01 | 64 | Armor | 0.4 | 0 |
| Hatch_L | 6 | Armor | 0.4 | 3 |
| Hatch_R | 6 | Armor | 0.4 | 3 |
| ShieldUpper_01 | 32 | Armor | 0.4 | 1 |
| ShieldWing_L | 32 | Armor | 0.4 | 1 |
| ShieldWing_R | 32 | Armor | 0.4 | 1 |
| Thruster_L_01 | 30 | Fragile | 1.2 | 7 |
| ShieldThruster_L_01 | 16 | Armor | 0.4 | 2 |
| Thruster_L_02 | 30 | Fragile | 1.2 | 7 |
| ShieldThruster_L_02 | 16 | Armor | 0.4 | 2 |
| Thruster_R_01 | 30 | Fragile | 1.2 | 7 |
| ShieldThruster_R_01 | 16 | Armor | 0.4 | 2 |
| Thruster_R_02 | 30 | Fragile | 1.2 | 7 |
| ShieldThruster_R_02 | 16 | Armor | 0.4 | 2 |
| WeaponAttachment | 1000 | Sturdy | 0.4 | 4 |
| Core | 167 | Critical | 1.5 | 9 |
| ShieldCore_01 | 32 | Armor | 0.4 | 1 |
| Weapon | 1000 | Sturdy | 0.4 | 8 |
| EyeDummyPart | — | — | — |  |

### Exact health assignment rules

| Rule | Tag query | HP | Matched parts |
| --- | --- | --- | --- |
| 0 | ID.Armor.Body | 64 | ShieldLower_01 |
| 1 | ID.Armor.Heavy | 32 | ShieldUpper_01, ShieldWing_L, ShieldWing_R, ShieldCore_01 |
| 2 | ID.Armor.Medium | 16 | ShieldThruster_L_01, ShieldThruster_L_02, ShieldThruster_R_01, ShieldThruster_R_02 |
| 3 | ID.Armor.Light | 6 | Hatch_L, Hatch_R |
| 4 | ALL(Group.Indestructible, NONE(ID.Weapon.Rifle)) | 1000 | WeaponAttachment |
| 5 | ID.Head | 1300 | Head |
| 6 | ID.Frame | 200 | Frame |
| 7 | ID.Thruster | 30 | Thruster_L_01, Thruster_L_02, Thruster_R_01, Thruster_R_02 |
| 8 | ID.Weapon.Rifle | 1000 | Weapon |
| 9 | ANY(ID.Core) | 167 | Core |

Some actor/style sources have partial-decoding warnings; the balancing health tables parsed separately. The JSON retains the warnings and recovered destruction settings.

<details>
<summary>Actual game source files</summary>

- [Content/Pioneer/Enemies/EliteDrone/Flamethrower/CS_EliteDrone_Flamethrower.json](../Sources/PioneerGame/Content/Pioneer/Enemies/EliteDrone/Flamethrower/CS_EliteDrone_Flamethrower.json)
- [Content/Pioneer/Enemies/EliteDrone/Flamethrower/C_EliteDrone_Flamethrower.json](../Sources/PioneerGame/Content/Pioneer/Enemies/EliteDrone/Flamethrower/C_EliteDrone_Flamethrower.json)
- [Content/Pioneer/Enemies/EliteDrone/Flamethrower/Capabilities/GA_EliteDrone_Flamethrower_Explosion.json](../Sources/PioneerGame/Content/Pioneer/Enemies/EliteDrone/Flamethrower/Capabilities/GA_EliteDrone_Flamethrower_Explosion.json)
- [Content/Pioneer/Enemies/EliteDrone/Flamethrower/DataAssets/CSSC_EliteDrone_FlameThrower.json](../Sources/PioneerGame/Content/Pioneer/Enemies/EliteDrone/Flamethrower/DataAssets/CSSC_EliteDrone_FlameThrower.json)
- [Content/Pioneer/Enemies/EliteDrone/Flamethrower/DataAssets/DA_Balancing_C_EliteDrone_Flamethrower.json](../Sources/PioneerGame/Content/Pioneer/Enemies/EliteDrone/Flamethrower/DataAssets/DA_Balancing_C_EliteDrone_Flamethrower.json)
- [Content/Pioneer/Enemies/EliteDrone/Flamethrower/DataAssets/DA_EnemyMetaData_EliteDrone_Flamethrower.json](../Sources/PioneerGame/Content/Pioneer/Enemies/EliteDrone/Flamethrower/DataAssets/DA_EnemyMetaData_EliteDrone_Flamethrower.json)
- [Content/Pioneer/Enemies/EliteDrone/Flamethrower/DataAssets/DA_EnemyType_EliteDrone_Flamethrower.json](../Sources/PioneerGame/Content/Pioneer/Enemies/EliteDrone/Flamethrower/DataAssets/DA_EnemyType_EliteDrone_Flamethrower.json)

</details>
