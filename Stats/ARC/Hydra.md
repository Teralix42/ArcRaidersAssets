# Hydra

[ARC stats](README.md) · [Machine-readable data](arc_parts.json) · [Damage model](Damage_Model.md)

**Configured frame rule:** 1050 HP. **Internal class:** `C_Kebab_Gatling`.

Frame HP is a balancing rule, not the sum of every limb or plate. Part rules and damage propagation are separate. `—` means unknown or unassigned.

[Interactive Blender inspection model](Models/Hydra.blend) · Native textures and inspector are packed into the file.

<a href="Renders/Hydra/01_Original_Materials_C.png"><img src="Renders/Hydra/01_Original_Materials_C.png" width="48%" alt="Hydra: Original Materials"></a>
<a href="Renders/Hydra/03_Part_Health_C.png"><img src="Renders/Hydra/03_Part_Health_C.png" width="48%" alt="Hydra: Part Health"></a>

### Layers and views

| Layer | Visible structure |
| --- | --- |
| A | Core + limb structure |
| B | Without armor |
| C | Full model |

<details>
<summary>All six views, including inner layers</summary>


**A: Core + limb structure**

<a href="Renders/Hydra/01_Original_Materials_A.png"><img src="Renders/Hydra/01_Original_Materials_A.png" width="32%" alt="Original Materials, layer A"></a>
<a href="Renders/Hydra/02_Part_Type_A.png"><img src="Renders/Hydra/02_Part_Type_A.png" width="32%" alt="Part Type, layer A"></a>
<a href="Renders/Hydra/03_Part_Health_A.png"><img src="Renders/Hydra/03_Part_Health_A.png" width="32%" alt="Part Health, layer A"></a>
<a href="Renders/Hydra/04_Break_Off_A.png"><img src="Renders/Hydra/04_Break_Off_A.png" width="32%" alt="Break Off, layer A"></a>
<a href="Renders/Hydra/05_Scavenge_Interaction_A.png"><img src="Renders/Hydra/05_Scavenge_Interaction_A.png" width="32%" alt="Scavenge Interaction, layer A"></a>
<a href="Renders/Hydra/06_Damage_Targets_A.png"><img src="Renders/Hydra/06_Damage_Targets_A.png" width="32%" alt="Damage Targets, layer A"></a>

**B: Without armor**

<a href="Renders/Hydra/01_Original_Materials_B.png"><img src="Renders/Hydra/01_Original_Materials_B.png" width="32%" alt="Original Materials, layer B"></a>
<a href="Renders/Hydra/02_Part_Type_B.png"><img src="Renders/Hydra/02_Part_Type_B.png" width="32%" alt="Part Type, layer B"></a>
<a href="Renders/Hydra/03_Part_Health_B.png"><img src="Renders/Hydra/03_Part_Health_B.png" width="32%" alt="Part Health, layer B"></a>
<a href="Renders/Hydra/04_Break_Off_B.png"><img src="Renders/Hydra/04_Break_Off_B.png" width="32%" alt="Break Off, layer B"></a>
<a href="Renders/Hydra/05_Scavenge_Interaction_B.png"><img src="Renders/Hydra/05_Scavenge_Interaction_B.png" width="32%" alt="Scavenge Interaction, layer B"></a>
<a href="Renders/Hydra/06_Damage_Targets_B.png"><img src="Renders/Hydra/06_Damage_Targets_B.png" width="32%" alt="Damage Targets, layer B"></a>

**C: Full model**

<a href="Renders/Hydra/01_Original_Materials_C.png"><img src="Renders/Hydra/01_Original_Materials_C.png" width="32%" alt="Original Materials, layer C"></a>
<a href="Renders/Hydra/02_Part_Type_C.png"><img src="Renders/Hydra/02_Part_Type_C.png" width="32%" alt="Part Type, layer C"></a>
<a href="Renders/Hydra/03_Part_Health_C.png"><img src="Renders/Hydra/03_Part_Health_C.png" width="32%" alt="Part Health, layer C"></a>
<a href="Renders/Hydra/04_Break_Off_C.png"><img src="Renders/Hydra/04_Break_Off_C.png" width="32%" alt="Break Off, layer C"></a>
<a href="Renders/Hydra/05_Scavenge_Interaction_C.png"><img src="Renders/Hydra/05_Scavenge_Interaction_C.png" width="32%" alt="Scavenge Interaction, layer C"></a>
<a href="Renders/Hydra/06_Damage_Targets_C.png"><img src="Renders/Hydra/06_Damage_Targets_C.png" width="32%" alt="Damage Targets, layer C"></a>

</details>

### Weak and critical parts

| Part | Configured HP | Group | Baseline physical damage × |
| --- | --- | --- | --- |
| Weakpoint_01 | 800 | WeakPoint | 1.5 |
| Weakpoint_02 | 800 | WeakPoint | 1.5 |
| Weakpoint_03 | 800 | WeakPoint | 1.5 |

### Every named part

These records also include sockets, bones, and proxy components; they are not all independent damageable hitboxes. The weapon’s separate ARC armor and weak-point multipliers still apply where indicated in JSON.

| Part | Configured HP | Resistance group | Physical damage × | Health rules |
| --- | --- | --- | --- | --- |
| GunTop_L_01_Muzzle | 280 | — | — | 3 |
| GunTop_R_01_Muzzle | 280 | — | — | 3 |
| GunMid_L_01_Muzzle | 280 | — | — | 3 |
| GunMid_R_01_Muzzle | 280 | — | — | 3 |
| GunBot_L_01_Muzzle | 280 | — | — | 3 |
| GunBot_R_01_Muzzle | 280 | — | — | 3 |
| Turret_01_Laser | — | — | — |  |
| Turret_02_Laser | — | — | — |  |
| Turret_03_Laser | — | — | — |  |
| DummyFrame | 9999 | Sturdy | 0.4 | 5 |
| Frame_01 | 1050 | Sturdy | 0.4 | 0 |
| CenterAxis_01 | 9999 | Sturdy | 0.4 | 5 |
| Head_01 | 9999 | Sturdy | 0.4 | 5 |
| Turret_01 | 550 | Sturdy | 0.4 | 1 |
| Armor_01 | 100 | Armor | 0.4 | 4 |
| GunTop_L_01 | 280 | Sturdy | 0.4 | 3 |
| GunTop_R_01 | 280 | Sturdy | 0.4 | 3 |
| Weakpoint_01 | 800 | WeakPoint | 1.5 | 2 |
| Turret_02 | 550 | Sturdy | 0.4 | 1 |
| Armor_02 | 100 | Armor | 0.4 | 4 |
| GunMid_L_01 | 280 | Sturdy | 0.4 | 3 |
| GunMid_R_01 | 280 | Sturdy | 0.4 | 3 |
| Weakpoint_02 | 800 | WeakPoint | 1.5 | 2 |
| Turret_03 | 550 | Sturdy | 0.4 | 1 |
| Armor_03 | 100 | Armor | 0.4 | 4 |
| GunBot_L_01 | 280 | Sturdy | 0.4 | 3 |
| GunBot_R_01 | 280 | Sturdy | 0.4 | 3 |
| Weakpoint_03 | 800 | WeakPoint | 1.5 | 2 |

### Exact health assignment rules

| Rule | Tag query | HP | Matched parts |
| --- | --- | --- | --- |
| 0 | ANY(ID.Frame) | 1050 | Frame_01 |
| 1 | ANY(ID.Joint) | 550 | Turret_01, Turret_02, Turret_03 |
| 2 | ANY(ID.Core) | 800 | Weakpoint_01, Weakpoint_02, Weakpoint_03 |
| 3 | ANY(ID.Weapon.GatlingGun) | 280 | GunTop_L_01_Muzzle, GunTop_R_01_Muzzle, GunMid_L_01_Muzzle, GunMid_R_01_Muzzle, GunBot_L_01_Muzzle, GunBot_R_01_Muzzle, GunTop_L_01, GunTop_R_01, GunMid_L_01, GunMid_R_01, GunBot_L_01, GunBot_R_01 |
| 4 | ID.Armor | 100 | Armor_01, Armor_02, Armor_03 |
| 5 | ANY(ID.DummyRoot, Group.Indestructible) | 9999 | DummyFrame, CenterAxis_01, Head_01 |

<details>
<summary>Actual game source files</summary>

- [Content/Pioneer/Enemies/Kebab/Gatling/Art/CSSC_Kebab_Gatling.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Kebab/Gatling/Art/CSSC_Kebab_Gatling.json)
- [Content/Pioneer/Enemies/Kebab/Gatling/C_Kebab_Gatling.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Kebab/Gatling/C_Kebab_Gatling.json)
- [Content/Pioneer/Enemies/Kebab/Gatling/DataAssets/DA_Balancing_C_Kebab_Gatling.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Kebab/Gatling/DataAssets/DA_Balancing_C_Kebab_Gatling.json)
- [Content/Pioneer/Enemies/Kebab/Gatling/DataAssets/DA_EnemyMetaData_Kebab_Gatling.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Kebab/Gatling/DataAssets/DA_EnemyMetaData_Kebab_Gatling.json)
- [Content/Pioneer/Enemies/Kebab/Gatling/DataAssets/DA_EnemyType_Kebab_Gatling.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Kebab/Gatling/DataAssets/DA_EnemyType_Kebab_Gatling.json)

</details>
