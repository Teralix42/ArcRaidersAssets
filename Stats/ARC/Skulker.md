# Skulker

[ARC stats](README.md) · [Damage model](Damage_Model.md)

**Configured frame rule:** 230 HP. **Internal class:** `C_Meerkat`.

Frame HP is assigned separately from part HP. A dash marks an unknown or unassigned value.

[Balancing and part HP](../Sources/PioneerGame/Content/Pioneer/Enemies/Meerkat/Meerkat/DataAssets/DA_Balancing_C_Meerkat.json) · [Enemy type](../Sources/PioneerGame/Content/Pioneer/Enemies/Meerkat/Meerkat/DataAssets/DA_EnemyType_Meerkat.json)

<details>
<summary>More game files</summary>

- [CS_Meerkat_SK.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Meerkat/Meerkat/CS_Meerkat_SK.json)
- [C_Meerkat.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Meerkat/Meerkat/C_Meerkat.json)
- [CSSC_Meerkat.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Meerkat/Meerkat/DataAssets/CSSC_Meerkat.json)
- [DA_EnemyMetaData_Meerkat.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Meerkat/Meerkat/DataAssets/DA_EnemyMetaData_Meerkat.json)

</details>

[Interactive Blender inspection model](Models/Skulker.blend) · Native textures and inspector are packed into the file.

<a href="Renders/Skulker/01_Original_Materials_B.png"><img src="Renders/Skulker/01_Original_Materials_B.png" width="48%" alt="Skulker: Original Materials"></a>
<a href="Renders/Skulker/03_Part_Health_B.png"><img src="Renders/Skulker/03_Part_Health_B.png" width="48%" alt="Skulker: Part Health"></a>

<details>
<summary>All stat renders</summary>

**Original materials**

<p align="center">
  <a href="Renders/Skulker/01_Original_Materials_A.png"><img src="Renders/Skulker/01_Original_Materials_A.png" width="47%" alt="Skulker original materials"></a>
  <a href="Renders/Skulker/01_Original_Materials_B.png"><img src="Renders/Skulker/01_Original_Materials_B.png" width="47%" alt="Skulker original materials"></a>
</p>

**Part type**

<p align="center">
  <a href="Renders/Skulker/02_Part_Type_A.png"><img src="Renders/Skulker/02_Part_Type_A.png" width="47%" alt="Skulker part type"></a>
  <a href="Renders/Skulker/02_Part_Type_B.png"><img src="Renders/Skulker/02_Part_Type_B.png" width="47%" alt="Skulker part type"></a>
</p>

**Part health**

<p align="center">
  <a href="Renders/Skulker/03_Part_Health_A.png"><img src="Renders/Skulker/03_Part_Health_A.png" width="47%" alt="Skulker part health"></a>
  <a href="Renders/Skulker/03_Part_Health_B.png"><img src="Renders/Skulker/03_Part_Health_B.png" width="47%" alt="Skulker part health"></a>
</p>

**Break-off parts**

<p align="center">
  <a href="Renders/Skulker/04_Break_Off_A.png"><img src="Renders/Skulker/04_Break_Off_A.png" width="47%" alt="Skulker break-off parts"></a>
  <a href="Renders/Skulker/04_Break_Off_B.png"><img src="Renders/Skulker/04_Break_Off_B.png" width="47%" alt="Skulker break-off parts"></a>
</p>

**Scavenging**

<p align="center">
  <a href="Renders/Skulker/05_Scavenge_Interaction_A.png"><img src="Renders/Skulker/05_Scavenge_Interaction_A.png" width="47%" alt="Skulker scavenging"></a>
  <a href="Renders/Skulker/05_Scavenge_Interaction_B.png"><img src="Renders/Skulker/05_Scavenge_Interaction_B.png" width="47%" alt="Skulker scavenging"></a>
</p>

**Damage targets**

<p align="center">
  <a href="Renders/Skulker/06_Damage_Targets_A.png"><img src="Renders/Skulker/06_Damage_Targets_A.png" width="47%" alt="Skulker damage targets"></a>
  <a href="Renders/Skulker/06_Damage_Targets_B.png"><img src="Renders/Skulker/06_Damage_Targets_B.png" width="47%" alt="Skulker damage targets"></a>
</p>

</details>

### Weak and critical parts

No explicit WeakPoint/Critical resistance assignment was recovered for this profile. This does not imply invulnerability.

### Outgoing damage rules

Configured values keyed by the part or attack tag. Attack timing and the final damage against a Raider depend on the attack and target.

| Tag | Damage type | Configured damage |
| --- | --- | --- |
| ID.Weapon.GatlingGun | Blunt | 12 |

### Every named part

This list includes mesh records such as sockets and proxies. See the [damage model](Damage_Model.md) for how weapon multipliers apply to each resistance group.

| Part | Configured HP | Resistance group | Physical damage × | Health rules |
| --- | --- | --- | --- | --- |
| Frame | 230 | Normal | 1 | 0 |
| Arm_01 | 10000 | Normal | 1 | 2 |
| Arm_02 | 10000 | Normal | 1 | 2 |
| Arm_03 | 10000 | Normal | 1 | 2 |
| Barrel_01 | 1000 | Normal | 1 | 1 |
| Hatch_R_01 | 13 | Normal | 1 | 6 |
| BodyArmor_L_01 | 28 | Normal | 1 | 5 |
| BodyArmor_R_01 | 28 | Normal | 1 | 5 |
| Head_01 | 10000 | Normal | 1 | 2 |
| LegUpper_L_01 | 125 | Normal | 1 | 3 |
| LegLower_L_01 | 125 | Normal | 1 | 3 |
| LegArmor_L_01 | 13 | Normal | 1 | 6 |
| LegArmor_L_02 | 13 | Normal | 1 | 6 |
| Thruster_L_01 | 40 | Fragile | 1.2 | 4 |
| Thruster_L_02 | 40 | Fragile | 1.2 | 4 |
| LegUpper_R_01 | 125 | Normal | 1 | 3 |
| LegLower_R_01 | 125 | Normal | 1 | 3 |
| LegArmor_R_01 | 13 | Normal | 1 | 6 |
| LegArmor_R_02 | 13 | Normal | 1 | 6 |
| Thruster_R_01 | 40 | Fragile | 1.2 | 4 |
| Thruster_R_02 | 40 | Fragile | 1.2 | 4 |
| Eye | — | — | — |  |

### Exact health assignment rules

| Rule | Tag query | HP | Matched parts |
| --- | --- | --- | --- |
| 0 | ID.Frame | 230 | Frame |
| 1 | ID.Weapon.GatlingGun | 1000 | Barrel_01 |
| 2 | ANY(ID.Arm, ID.Head) | 10000 | Arm_01, Arm_02, Arm_03, Head_01 |
| 3 | ID.Leg | 125 | LegUpper_L_01, LegLower_L_01, LegUpper_R_01, LegLower_R_01 |
| 4 | ID.Thruster | 40 | Thruster_L_01, Thruster_L_02, Thruster_R_01, Thruster_R_02 |
| 5 | ID.Armor.Medium | 28 | BodyArmor_L_01, BodyArmor_R_01 |
| 6 | ID.Armor.Light | 13 | Hatch_R_01, LegArmor_L_01, LegArmor_L_02, LegArmor_R_01, LegArmor_R_02 |

<details>
<summary>Destruction and stun rules</summary>

**Destruction groups**

| Part query | Destruction damage | Max level | Game file |
| --- | --- | --- | --- |
| ANY(ID.Arm) | 50 | 1 | [Actor config](../Sources/PioneerGame/Content/Pioneer/Enemies/Meerkat/Meerkat/C_Meerkat.json) |

**Chain destruction**

| Trigger part | Configured threshold | Parts destroyed |
| --- | --- | --- |
| Thruster_R_01 | 1% HP | LegArmor_R_01 |
| Thruster_L_01 | 1% HP | LegArmor_L_01 |
| Thruster_R_02 | 1% HP | LegArmor_R_02 |
| Thruster_L_02 | 1% HP | LegArmor_L_02 |

**Stun propagation**

| Source part query | Destination part query |
| --- | --- |
| ID.Frame | ALL(ID.Wheel, Group.Relative.Middle) |

</details>
