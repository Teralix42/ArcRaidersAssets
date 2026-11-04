# Vaporizer

[ARC stats](README.md) · [Machine-readable data](arc_parts.json) · [Damage model](Damage_Model.md)

**Configured frame rule:** 1500 HP. **Internal class:** `C_HeavyDrone_Laser`.

Frame HP is a balancing rule, not the sum of every limb or plate. Part rules and damage propagation are separate. `—` means unknown or unassigned.

[Interactive Blender inspection model](Models/Vaporizer.blend) · Native textures and inspector are packed into the file.

<a href="Renders/Vaporizer/01_Original_Materials_C.png"><img src="Renders/Vaporizer/01_Original_Materials_C.png" width="48%" alt="Vaporizer: Original Materials"></a>
<a href="Renders/Vaporizer/03_Part_Health_C.png"><img src="Renders/Vaporizer/03_Part_Health_C.png" width="48%" alt="Vaporizer: Part Health"></a>

### Layers and views

| Layer | Visible structure |
| --- | --- |
| A | Core + limb structure |
| B | Without armor |
| C | Full model |

<details>
<summary>All six views, including inner layers</summary>


**A: Core + limb structure**

<a href="Renders/Vaporizer/01_Original_Materials_A.png"><img src="Renders/Vaporizer/01_Original_Materials_A.png" width="32%" alt="Original Materials, layer A"></a>
<a href="Renders/Vaporizer/02_Part_Type_A.png"><img src="Renders/Vaporizer/02_Part_Type_A.png" width="32%" alt="Part Type, layer A"></a>
<a href="Renders/Vaporizer/03_Part_Health_A.png"><img src="Renders/Vaporizer/03_Part_Health_A.png" width="32%" alt="Part Health, layer A"></a>
<a href="Renders/Vaporizer/04_Break_Off_A.png"><img src="Renders/Vaporizer/04_Break_Off_A.png" width="32%" alt="Break Off, layer A"></a>
<a href="Renders/Vaporizer/05_Scavenge_Interaction_A.png"><img src="Renders/Vaporizer/05_Scavenge_Interaction_A.png" width="32%" alt="Scavenge Interaction, layer A"></a>
<a href="Renders/Vaporizer/06_Damage_Targets_A.png"><img src="Renders/Vaporizer/06_Damage_Targets_A.png" width="32%" alt="Damage Targets, layer A"></a>

**B: Without armor**

<a href="Renders/Vaporizer/01_Original_Materials_B.png"><img src="Renders/Vaporizer/01_Original_Materials_B.png" width="32%" alt="Original Materials, layer B"></a>
<a href="Renders/Vaporizer/02_Part_Type_B.png"><img src="Renders/Vaporizer/02_Part_Type_B.png" width="32%" alt="Part Type, layer B"></a>
<a href="Renders/Vaporizer/03_Part_Health_B.png"><img src="Renders/Vaporizer/03_Part_Health_B.png" width="32%" alt="Part Health, layer B"></a>
<a href="Renders/Vaporizer/04_Break_Off_B.png"><img src="Renders/Vaporizer/04_Break_Off_B.png" width="32%" alt="Break Off, layer B"></a>
<a href="Renders/Vaporizer/05_Scavenge_Interaction_B.png"><img src="Renders/Vaporizer/05_Scavenge_Interaction_B.png" width="32%" alt="Scavenge Interaction, layer B"></a>
<a href="Renders/Vaporizer/06_Damage_Targets_B.png"><img src="Renders/Vaporizer/06_Damage_Targets_B.png" width="32%" alt="Damage Targets, layer B"></a>

**C: Full model**

<a href="Renders/Vaporizer/01_Original_Materials_C.png"><img src="Renders/Vaporizer/01_Original_Materials_C.png" width="32%" alt="Original Materials, layer C"></a>
<a href="Renders/Vaporizer/02_Part_Type_C.png"><img src="Renders/Vaporizer/02_Part_Type_C.png" width="32%" alt="Part Type, layer C"></a>
<a href="Renders/Vaporizer/03_Part_Health_C.png"><img src="Renders/Vaporizer/03_Part_Health_C.png" width="32%" alt="Part Health, layer C"></a>
<a href="Renders/Vaporizer/04_Break_Off_C.png"><img src="Renders/Vaporizer/04_Break_Off_C.png" width="32%" alt="Break Off, layer C"></a>
<a href="Renders/Vaporizer/05_Scavenge_Interaction_C.png"><img src="Renders/Vaporizer/05_Scavenge_Interaction_C.png" width="32%" alt="Scavenge Interaction, layer C"></a>
<a href="Renders/Vaporizer/06_Damage_Targets_C.png"><img src="Renders/Vaporizer/06_Damage_Targets_C.png" width="32%" alt="Damage Targets, layer C"></a>

</details>

### Weak and critical parts

| Part | Configured HP | Group | Baseline physical damage × |
| --- | --- | --- | --- |
| Core | 1340 | Critical | 1.5 |

### Every named part

These records also include sockets, bones, and proxy components; they are not all independent damageable hitboxes. The weapon’s separate ARC armor and weak-point multipliers still apply where indicated in JSON.

| Part | Configured HP | Resistance group | Physical damage × | Health rules |
| --- | --- | --- | --- | --- |
| Muzzle | — | — | — |  |
| Thruster_L_01_Socket | — | — | — |  |
| Thruster_L_02_Socket | — | — | — |  |
| Thruster_R_01_Socket | — | — | — |  |
| Thruster_R_02_Socket | — | — | — |  |
| ThrusterPart_L_01_Socket | — | — | — |  |
| ThrusterPart_L_02_Socket | — | — | — |  |
| ThrusterPart_L_03_Socket | — | — | — |  |
| ThrusterPart_L_04_Socket | — | — | — |  |
| ThrusterPart_R_01_Socket | — | — | — |  |
| ThrusterPart_R_02_Socket | — | — | — |  |
| ThrusterPart_R_03_Socket | — | — | — |  |
| ThrusterPart_R_04_Socket | — | — | — |  |
| Frame | 1500 | Sturdy | 0.4 | 0 |
| ArmorHeavy_01_L | 60 | Armor | 0.4 | 4 |
| ArmorHeavy_01_R | 60 | Armor | 0.4 | 4 |
| ArmorHeavy_02_L | 60 | Armor | 0.4 | 4 |
| ArmorHeavy_02_R | 60 | Armor | 0.4 | 4 |
| ArmorHeavy_03_L | 60 | Armor | 0.4 | 4 |
| ArmorHeavy_03_R | 60 | Armor | 0.4 | 4 |
| ArmorHeavy_04_L | 60 | Armor | 0.4 | 4 |
| ArmorHeavy_04_R | 60 | Armor | 0.4 | 4 |
| ArmorHeavy_05 | 60 | Armor | 0.4 | 4 |
| ArmorLight_01_L | 240 | Normal | 1 | 2 |
| ArmorLight_01_R | 240 | Normal | 1 | 2 |
| ArmorLight_02_L | 240 | Normal | 1 | 2 |
| ArmorLight_02_R | 240 | Normal | 1 | 2 |
| ArmorLight_03 | 240 | Normal | 1 | 2 |
| Core | 1340 | Critical | 1.5 | 10 |
| Eye | 1340 | Fragile | 1.2 | 10 |
| Flap_01_L | 20 | Armor | 0.4 | 3 |
| Flap_01_R | 20 | Armor | 0.4 | 3 |
| Flap_02_L | 20 | Armor | 0.4 | 3 |
| Flap_02_R | 20 | Armor | 0.4 | 3 |
| Flap_03_L | 20 | Armor | 0.4 | 3 |
| Flap_03_R | 20 | Armor | 0.4 | 3 |
| Hatch | 200 | Normal | 1 | 1 |
| ThrusterRoot_L_01 | 104 | Sturdy | 0.4 | 5 |
| ThrusterPart_L_01 | 114 | Fragile | 1.2 | 6 |
| ThrusterArmor_L_01 | 28 | Normal | 1 | 7 |
| ThrusterPart_L_02 | 114 | Fragile | 1.2 | 6 |
| ThrusterArmor_L_02 | 28 | Normal | 1 | 7 |
| ThrusterRoot_L_02 | 104 | Sturdy | 0.4 | 5 |
| ThrusterPart_L_03 | 114 | Fragile | 1.2 | 6 |
| ThrusterArmor_L_03 | 28 | Normal | 1 | 7 |
| ThrusterPart_L_04 | 114 | Fragile | 1.2 | 6 |
| ThrusterArmor_L_04 | 28 | Normal | 1 | 7 |
| ThrusterRoot_R_01 | 104 | Sturdy | 0.4 | 5 |
| ThrusterPart_R_01 | 114 | Fragile | 1.2 | 6 |
| ThrusterArmor_R_01 | 28 | Normal | 1 | 7 |
| ThrusterPart_R_02 | 114 | Fragile | 1.2 | 6 |
| ThrusterArmor_R_02 | 28 | Normal | 1 | 7 |
| ThrusterRoot_R_02 | 104 | Sturdy | 0.4 | 5 |
| ThrusterPart_R_03 | 114 | Fragile | 1.2 | 6 |
| ThrusterArmor_R_03 | 28 | Normal | 1 | 7 |
| ThrusterPart_R_04 | 114 | Fragile | 1.2 | 6 |
| ThrusterArmor_R_04 | 28 | Normal | 1 | 7 |
| Weapon | 10000 | Sturdy | 0.4 | 9 |
| WeaponBarrel | 10000 | Sturdy | 0.4 | 8 |
| WeaponHatch | 10000 | Sturdy | 0.4 | 9 |

### Exact health assignment rules

| Rule | Tag query | HP | Matched parts |
| --- | --- | --- | --- |
| 0 | ID.Frame | 1500 | Frame |
| 1 | ID.Hatch | 200 | Hatch |
| 2 | ID.Armor.Light | 240 | ArmorLight_01_L, ArmorLight_01_R, ArmorLight_02_L, ArmorLight_02_R, ArmorLight_03 |
| 3 | ID.Flap | 20 | Flap_01_L, Flap_01_R, Flap_02_L, Flap_02_R, Flap_03_L, Flap_03_R |
| 4 | ID.Armor.Heavy | 60 | ArmorHeavy_01_L, ArmorHeavy_01_R, ArmorHeavy_02_L, ArmorHeavy_02_R, ArmorHeavy_03_L, ArmorHeavy_03_R, ArmorHeavy_04_L, ArmorHeavy_04_R, ArmorHeavy_05 |
| 5 | ID.Thruster | 104 | ThrusterRoot_L_01, ThrusterRoot_L_02, ThrusterRoot_R_01, ThrusterRoot_R_02 |
| 6 | Part.HealthGroup.Thruster | 114 | ThrusterPart_L_01, ThrusterPart_L_02, ThrusterPart_L_03, ThrusterPart_L_04, ThrusterPart_R_01, ThrusterPart_R_02, ThrusterPart_R_03, ThrusterPart_R_04 |
| 7 | Part.HealthGroup.Armor | 28 | ThrusterArmor_L_01, ThrusterArmor_L_02, ThrusterArmor_L_03, ThrusterArmor_L_04, ThrusterArmor_R_01, ThrusterArmor_R_02, ThrusterArmor_R_03, ThrusterArmor_R_04 |
| 8 | ID.Weapon.Laser | 10000 | WeaponBarrel |
| 9 | ALL(Group.Indestructible, NONE(ID.Weapon.Laser)) | 10000 | Weapon, WeaponHatch |
| 10 | Group.Critical | 1340 | Core, Eye |

<details>
<summary>Actual game source files</summary>

- [Content/Pioneer/Enemies/HeavyDrone/HeavyDroneLaser/C_HeavyDrone_Laser.json](../Sources/PioneerGame/Content/Pioneer/Enemies/HeavyDrone/HeavyDroneLaser/C_HeavyDrone_Laser.json)
- [Content/Pioneer/Enemies/HeavyDrone/HeavyDroneLaser/DataAssets/CSSC_HeavyDroneLaser.json](../Sources/PioneerGame/Content/Pioneer/Enemies/HeavyDrone/HeavyDroneLaser/DataAssets/CSSC_HeavyDroneLaser.json)
- [Content/Pioneer/Enemies/HeavyDrone/HeavyDroneLaser/DataAssets/DA_Balancing_C_HeavyDrone_Laser.json](../Sources/PioneerGame/Content/Pioneer/Enemies/HeavyDrone/HeavyDroneLaser/DataAssets/DA_Balancing_C_HeavyDrone_Laser.json)
- [Content/Pioneer/Enemies/HeavyDrone/HeavyDroneLaser/DataAssets/DA_EnemyMetaData_HeavyDroneLaser.json](../Sources/PioneerGame/Content/Pioneer/Enemies/HeavyDrone/HeavyDroneLaser/DataAssets/DA_EnemyMetaData_HeavyDroneLaser.json)
- [Content/Pioneer/Enemies/HeavyDrone/HeavyDroneLaser/DataAssets/DA_EnemyType_HeavyDrone_Laser.json](../Sources/PioneerGame/Content/Pioneer/Enemies/HeavyDrone/HeavyDroneLaser/DataAssets/DA_EnemyType_HeavyDrone_Laser.json)

</details>
