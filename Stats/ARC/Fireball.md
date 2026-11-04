# Fireball

[ARC stats](README.md) · [Machine-readable data](arc_parts.json) · [Damage model](Damage_Model.md)

**Configured frame rule:** 20 HP. **Internal class:** `C_RollBot_Flamethrower`.

Frame HP is a balancing rule, not the sum of every limb or plate. Part rules and damage propagation are separate. `—` means unknown or unassigned.

[Interactive Blender inspection model](Models/Fireball.blend) · Native textures and inspector are packed into the file.

<a href="Renders/Fireball/01_Original_Materials_B.png"><img src="Renders/Fireball/01_Original_Materials_B.png" width="48%" alt="Fireball: Original Materials"></a>
<a href="Renders/Fireball/03_Part_Health_B.png"><img src="Renders/Fireball/03_Part_Health_B.png" width="48%" alt="Fireball: Part Health"></a>

### Layers and views

| Layer | Visible structure |
| --- | --- |
| A | Without armor |
| B | Full model |

<details>
<summary>All six views, including inner layers</summary>


**A: Without armor**

<a href="Renders/Fireball/01_Original_Materials_A.png"><img src="Renders/Fireball/01_Original_Materials_A.png" width="32%" alt="Original Materials, layer A"></a>
<a href="Renders/Fireball/02_Part_Type_A.png"><img src="Renders/Fireball/02_Part_Type_A.png" width="32%" alt="Part Type, layer A"></a>
<a href="Renders/Fireball/03_Part_Health_A.png"><img src="Renders/Fireball/03_Part_Health_A.png" width="32%" alt="Part Health, layer A"></a>
<a href="Renders/Fireball/04_Break_Off_A.png"><img src="Renders/Fireball/04_Break_Off_A.png" width="32%" alt="Break Off, layer A"></a>
<a href="Renders/Fireball/05_Scavenge_Interaction_A.png"><img src="Renders/Fireball/05_Scavenge_Interaction_A.png" width="32%" alt="Scavenge Interaction, layer A"></a>
<a href="Renders/Fireball/06_Damage_Targets_A.png"><img src="Renders/Fireball/06_Damage_Targets_A.png" width="32%" alt="Damage Targets, layer A"></a>

**B: Full model**

<a href="Renders/Fireball/01_Original_Materials_B.png"><img src="Renders/Fireball/01_Original_Materials_B.png" width="32%" alt="Original Materials, layer B"></a>
<a href="Renders/Fireball/02_Part_Type_B.png"><img src="Renders/Fireball/02_Part_Type_B.png" width="32%" alt="Part Type, layer B"></a>
<a href="Renders/Fireball/03_Part_Health_B.png"><img src="Renders/Fireball/03_Part_Health_B.png" width="32%" alt="Part Health, layer B"></a>
<a href="Renders/Fireball/04_Break_Off_B.png"><img src="Renders/Fireball/04_Break_Off_B.png" width="32%" alt="Break Off, layer B"></a>
<a href="Renders/Fireball/05_Scavenge_Interaction_B.png"><img src="Renders/Fireball/05_Scavenge_Interaction_B.png" width="32%" alt="Scavenge Interaction, layer B"></a>
<a href="Renders/Fireball/06_Damage_Targets_B.png"><img src="Renders/Fireball/06_Damage_Targets_B.png" width="32%" alt="Damage Targets, layer B"></a>

</details>

### Weak and critical parts

| Part | Configured HP | Group | Baseline physical damage × |
| --- | --- | --- | --- |
| Frame_01 | 20 | Critical | 1.5 |

### Every named part

These records also include sockets, bones, and proxy components; they are not all independent damageable hitboxes. The weapon’s separate ARC armor and weak-point multipliers still apply where indicated in JSON.

| Part | Configured HP | Resistance group | Physical damage × | Health rules |
| --- | --- | --- | --- | --- |
| DummyParent_Root | 1000 | Normal | 1 | 3 |
| Armor_01_A_01 | 10 | Armor | 0.4 | 0 |
| Armor_01_A_02 | 10 | Armor | 0.4 | 0 |
| Frame_01 | 20 | Critical | 1.5 | 2 |
| FrameCenterAxis | — | Normal | 1 |  |
| Arm_L_01 | 100 | Sturdy | 0.4 | 1 |
| Ear_01_A | 10 | Armor | 0.4 | 0 |
| Arm_R_01 | 100 | Sturdy | 0.4 | 1 |
| Ear_01_B | 10 | Armor | 0.4 | 0 |
| Scanner | — | Normal | 1 |  |
| PerceptionPart | — | Normal | 1 |  |

### Exact health assignment rules

| Rule | Tag query | HP | Matched parts |
| --- | --- | --- | --- |
| 0 | ID.Armor.Heavy | 10 | Armor_01_A_01, Armor_01_A_02, Ear_01_A, Ear_01_B |
| 1 | ID.Weapon.Dispenser | 100 | Arm_L_01, Arm_R_01 |
| 2 | ID.Frame | 20 | Frame_01 |
| 3 | ID.Rollbot.Root | 1000 | DummyParent_Root |

Some actor/style sources have partial-decoding warnings; the balancing health tables parsed separately. The JSON retains the warnings and recovered destruction settings.

<details>
<summary>Actual game source files</summary>

- [Content/Pioneer/Enemies/FireBall/C_RollBot_Flamethrower.json](../Sources/PioneerGame/Content/Pioneer/Enemies/FireBall/C_RollBot_Flamethrower.json)
- [Content/Pioneer/Enemies/FireBall/Capabilities/GA_RollbotFlamethrower_Explosion.json](../Sources/PioneerGame/Content/Pioneer/Enemies/FireBall/Capabilities/GA_RollbotFlamethrower_Explosion.json)
- [Content/Pioneer/Enemies/FireBall/DataAssets/CSSC_RollBot_Flamethrower.json](../Sources/PioneerGame/Content/Pioneer/Enemies/FireBall/DataAssets/CSSC_RollBot_Flamethrower.json)
- [Content/Pioneer/Enemies/FireBall/DataAssets/DA_Balancing_C_RollBot_Flamethrower.json](../Sources/PioneerGame/Content/Pioneer/Enemies/FireBall/DataAssets/DA_Balancing_C_RollBot_Flamethrower.json)
- [Content/Pioneer/Enemies/FireBall/DataAssets/DA_EnemyMetaData_RollBot_Flamethrower.json](../Sources/PioneerGame/Content/Pioneer/Enemies/FireBall/DataAssets/DA_EnemyMetaData_RollBot_Flamethrower.json)
- [Content/Pioneer/Enemies/FireBall/DataAssets/DA_EnemyType_RollBot_Flamethrower.json](../Sources/PioneerGame/Content/Pioneer/Enemies/FireBall/DataAssets/DA_EnemyType_RollBot_Flamethrower.json)

</details>
