# Bully

[ARC stats](README.md) · [Damage model](Damage_Model.md)

**Configured frame rule:** 3000 HP. **Internal class:** `C_Tarragon_01`.

Frame HP is assigned separately from part HP. A dash marks an unknown or unassigned value.

[Balancing and part HP](../Sources/PioneerGame/Content/Pioneer/Enemies/Tarragon/DataAssets/DA_Balancing_C_Tarragon_01.json) · [Enemy type](../Sources/PioneerGame/Content/Pioneer/Enemies/Tarragon/DataAssets/DA_EnemyType_Tarragon_01.json)

<details>
<summary>More game files</summary>

- [CSSM_Tarragon_01.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Tarragon/CSSM_Tarragon_01.json)
- [C_Tarragon_01.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Tarragon/C_Tarragon_01.json)
- [DA_EnemyMetaData_Tarragon.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Tarragon/DataAssets/DA_EnemyMetaData_Tarragon.json)

</details>

[Interactive Blender inspection model](Models/Bully.blend) · Native textures and inspector are packed into the file.

<a href="Renders/Bully/01_Original_Materials_C.png"><img src="Renders/Bully/01_Original_Materials_C.png" width="48%" alt="Bully: Original Materials"></a>
<a href="Renders/Bully/03_Part_Health_C.png"><img src="Renders/Bully/03_Part_Health_C.png" width="48%" alt="Bully: Part Health"></a>

<details>
<summary>All stat renders</summary>

**Original materials**

<p align="center">
  <a href="Renders/Bully/01_Original_Materials_B.png"><img src="Renders/Bully/01_Original_Materials_B.png" width="47%" alt="Bully original materials"></a>
  <a href="Renders/Bully/01_Original_Materials_C.png"><img src="Renders/Bully/01_Original_Materials_C.png" width="47%" alt="Bully original materials"></a>
</p>

**Part type**

<p align="center">
  <a href="Renders/Bully/02_Part_Type_B.png"><img src="Renders/Bully/02_Part_Type_B.png" width="47%" alt="Bully part type"></a>
  <a href="Renders/Bully/02_Part_Type_C.png"><img src="Renders/Bully/02_Part_Type_C.png" width="47%" alt="Bully part type"></a>
</p>

**Part health**

<p align="center">
  <a href="Renders/Bully/03_Part_Health_B.png"><img src="Renders/Bully/03_Part_Health_B.png" width="47%" alt="Bully part health"></a>
  <a href="Renders/Bully/03_Part_Health_C.png"><img src="Renders/Bully/03_Part_Health_C.png" width="47%" alt="Bully part health"></a>
</p>

**Break-off parts**

<p align="center">
  <a href="Renders/Bully/04_Break_Off_B.png"><img src="Renders/Bully/04_Break_Off_B.png" width="47%" alt="Bully break-off parts"></a>
  <a href="Renders/Bully/04_Break_Off_C.png"><img src="Renders/Bully/04_Break_Off_C.png" width="47%" alt="Bully break-off parts"></a>
</p>

**Scavenging**

<p align="center">
  <a href="Renders/Bully/05_Scavenge_Interaction_B.png"><img src="Renders/Bully/05_Scavenge_Interaction_B.png" width="47%" alt="Bully scavenging"></a>
  <a href="Renders/Bully/05_Scavenge_Interaction_C.png"><img src="Renders/Bully/05_Scavenge_Interaction_C.png" width="47%" alt="Bully scavenging"></a>
</p>

**Damage targets**

<p align="center">
  <a href="Renders/Bully/06_Damage_Targets_B.png"><img src="Renders/Bully/06_Damage_Targets_B.png" width="47%" alt="Bully damage targets"></a>
  <a href="Renders/Bully/06_Damage_Targets_C.png"><img src="Renders/Bully/06_Damage_Targets_C.png" width="47%" alt="Bully damage targets"></a>
</p>

</details>

### Weak and critical parts

| Part | Configured HP | Group | Baseline physical damage × |
| --- | --- | --- | --- |
| WeakpointHead | 9999 | WeakPoint | 1.5 |
| Weakpoint_01_L_01 | 400 | WeakPoint | 1.5 |
| Weakpoint_01_R_01 | 400 | WeakPoint | 1.5 |
| Weakpoint_01_L_02 | 400 | WeakPoint | 1.5 |
| Weakpoint_01_R_02 | 400 | WeakPoint | 1.5 |

### Outgoing damage rules

Configured values keyed by the part or attack tag. Attack timing and the final damage against a Raider depend on the attack and target.

| Tag | Damage type | Configured damage |
| --- | --- | --- |
| ID.Frame | Blunt | 85 |
| ID.Weapon.Shotgun | Blunt | 15 |

### Every named part

This list includes mesh records such as sockets and proxies. See the [damage model](Damage_Model.md) for how weapon multipliers apply to each resistance group.

| Part | Configured HP | Resistance group | Physical damage × | Health rules |
| --- | --- | --- | --- | --- |
| Muzzle | — | — | — |  |
| LauncherMuzzle | — | — | — |  |
| VisionCone | — | — | — |  |
| FirePatchMuzzle | — | — | — |  |
| Body_01 | 3000 | Sturdy | 0.4 | 0 |
| Armor_01_L | 90 | Armor | 0.4 | 10 |
| Armor_01_R | 90 | Armor | 0.4 | 10 |
| Armor_02_L | 90 | Armor | 0.4 | 10 |
| Armor_02_R | 90 | Armor | 0.4 | 10 |
| Armor_03_L | 48 | Armor | 0.4 | 8 |
| Armor_03_R | 48 | Armor | 0.4 | 8 |
| Armor_04 | 90 | Armor | 0.4 | 10 |
| Armor_05 | 48 | Armor | 0.4 | 8 |
| Armor_06_L | 48 | Armor | 0.4 | 8 |
| Armor_06_R | 48 | Armor | 0.4 | 8 |
| Inside_01_L | 400 | Fragile | 1.2 | 17 |
| Inside_01_R | 400 | Fragile | 1.2 | 17 |
| Inside_02_L | 400 | Fragile | 1.2 | 17 |
| Inside_02_R | 400 | Fragile | 1.2 | 17 |
| Inside_03 | 400 | Fragile | 1.2 | 17 |
| Inside_04 | 400 | Fragile | 1.2 | 17 |
| Neck_01 | 10000 | Normal | 1 | 6 |
| NeckPivot_01 | 99999999 | Normal | 1 | 7 |
| HeadPivot | 10000000 | Normal | 1 | 4 |
| Head_01 | 1600 | Normal | 1 | 3 |
| Eye_01 | 9999 | Fragile | 1.2 | 12 |
| Flap_01_C_01 | 48 | Armor | 0.4 | 9 |
| Flap_01_C_02 | 48 | Armor | 0.4 | 9 |
| Flap_02_L | 48 | Armor | 0.4 | 9 |
| Flap_02_R | 48 | Armor | 0.4 | 9 |
| Gun | 999999 | Sturdy | 0.4 | 15 |
| HeadArmor_01_L | 48 | Armor | 0.4 | 9 |
| HeadArmor_01_R | 48 | Armor | 0.4 | 9 |
| RocketLauncher | 999999 | Sturdy | 0.4 | 14 |
| RocketLauncherLock | 48 | Sturdy | 0.4 | 9 |
| WeakpointHead | 9999 | WeakPoint | 1.5 | 11 |
| UpperLeg_01_L | 500 | Fragile | 1.2 | 1 |
| LowerLeg_01_L | 400 | Fragile | 1.2 | 2 |
| Foot_L_01 | 1000 | Sturdy | 0.4 | 5 |
| FootCol_01_L | 999999 | Sturdy | 0.4 | 13 |
| LowerLeg_01_Armor_01_L | 48 | Armor | 0.4 | 8 |
| UpperLeg_01_Armor_01_L | 48 | Armor | 0.4 | 8 |
| Weakpoint_01_L_01 | 400 | WeakPoint | 1.5 | 16 |
| UpperLeg_01_R | 500 | Fragile | 1.2 | 1 |
| LowerLeg_01_R | 400 | Fragile | 1.2 | 2 |
| Foot_R_01 | 1000 | Sturdy | 0.4 | 5 |
| FootCol_01_R | 999999 | Sturdy | 0.4 | 13 |
| LowerLeg_01_Armor_01_R | 48 | Armor | 0.4 | 8 |
| UpperLeg_01_Armor_01_R | 48 | Armor | 0.4 | 8 |
| Weakpoint_01_R_01 | 400 | WeakPoint | 1.5 | 16 |
| UpperLeg_02_L | 500 | Fragile | 1.2 | 1 |
| LowerLeg_02_L | 400 | Fragile | 1.2 | 2 |
| Foot_L_02 | 1000 | Sturdy | 0.4 | 5 |
| FootCol_02_L | 999999 | Sturdy | 0.4 | 13 |
| LowerLeg_02_Armor_01_L | 48 | Armor | 0.4 | 8 |
| UpperLeg_02_Armor_01_L | 48 | Armor | 0.4 | 8 |
| Weakpoint_01_L_02 | 400 | WeakPoint | 1.5 | 16 |
| UpperLeg_02_R | 500 | Fragile | 1.2 | 1 |
| LowerLeg_02_R | 400 | Fragile | 1.2 | 2 |
| Foot_R_02 | 1000 | Sturdy | 0.4 | 5 |
| FootCol_02_R | 999999 | Sturdy | 0.4 | 13 |
| LowerLeg_02_Armor_01_R | 48 | Armor | 0.4 | 8 |
| UpperLeg_02_Armor_01_R | 48 | Armor | 0.4 | 8 |
| Weakpoint_01_R_02 | 400 | WeakPoint | 1.5 | 16 |

### Exact health assignment rules

| Rule | Tag query | HP | Matched parts |
| --- | --- | --- | --- |
| 0 | ID.Frame | 3000 | Body_01 |
| 1 | ALL(ID.Leg, Group.Relative.Upper) | 500 | UpperLeg_01_L, UpperLeg_01_R, UpperLeg_02_L, UpperLeg_02_R |
| 2 | ALL(ID.Leg, Group.Relative.Lower) | 400 | LowerLeg_01_L, LowerLeg_01_R, LowerLeg_02_L, LowerLeg_02_R |
| 3 | ID.Head | 1600 | Head_01 |
| 4 | ID.HeadPivot | 10000000 | HeadPivot |
| 5 | ID.Foot | 1000 | Foot_L_01, Foot_R_01, Foot_L_02, Foot_R_02 |
| 6 | ID.Neck | 10000 | Neck_01 |
| 7 | ID.NeckPivot | 99999999 | NeckPivot_01 |
| 8 | ID.Armor.Light | 48 | Armor_03_L, Armor_03_R, Armor_05, Armor_06_L, Armor_06_R, LowerLeg_01_Armor_01_L, UpperLeg_01_Armor_01_L, LowerLeg_01_Armor_01_R, UpperLeg_01_Armor_01_R, LowerLeg_02_Armor_01_L, UpperLeg_02_Armor_01_L, LowerLeg_02_Armor_01_R, UpperLeg_02_Armor_01_R |
| 9 | ID.Armor.Head | 48 | Flap_01_C_01, Flap_01_C_02, Flap_02_L, Flap_02_R, HeadArmor_01_L, HeadArmor_01_R, RocketLauncherLock |
| 10 | ID.Armor.Heavy | 90 | Armor_01_L, Armor_01_R, Armor_02_L, Armor_02_R, Armor_04 |
| 11 | ALL(Group.Weakpoint, NONE(ID.Joint)) | 9999 | WeakpointHead |
| 12 | ID.Eye | 9999 | Eye_01 |
| 13 | ID.FootCollision | 999999 | FootCol_01_L, FootCol_01_R, FootCol_02_L, FootCol_02_R |
| 14 | ID.Weapon.Grenade | 999999 | RocketLauncher |
| 15 | ID.Weapon.Shotgun | 999999 | Gun |
| 16 | ID.Joint | 400 | Weakpoint_01_L_01, Weakpoint_01_R_01, Weakpoint_01_L_02, Weakpoint_01_R_02 |
| 17 | ID.Interior | 400 | Inside_01_L, Inside_01_R, Inside_02_L, Inside_02_R, Inside_03, Inside_04 |

<details>
<summary>Destruction and stun rules</summary>

**Chain destruction**

| Trigger part | Configured threshold | Parts destroyed |
| --- | --- | --- |
| Weakpoint_01_L_01 | 1% HP | LowerLeg_01_L |
| Weakpoint_01_L_02 | 1% HP | LowerLeg_02_L |
| Weakpoint_01_R_01 | 1% HP | LowerLeg_01_R |
| Weakpoint_01_R_02 | 1% HP | LowerLeg_02_R |

**Damage triggers**

| Trigger part | Condition | Effect |
| --- | --- | --- |
| Head_01 | Part break | Enraged |

**Stun propagation**

| Source part query | Destination part query |
| --- | --- |
| ALL(ID.Leg, Group.Relative.Front, Group.Relative.Left, Group.Relative.Upper) | ALL(ID.Leg, Group.Relative.Front, Group.Relative.Left, Group.Relative.Lower) |
| ALL(ID.Leg, Group.Relative.Front, Group.Relative.Right, Group.Relative.Upper) | ALL(ID.Leg, Group.Relative.Front, Group.Relative.Right, Group.Relative.Lower) |
| ALL(ID.Leg, Group.Relative.Left, Group.Relative.Rear, Group.Relative.Upper) | ALL(ID.Leg, Group.Relative.Left, Group.Relative.Rear, Group.Relative.Lower) |
| ALL(ID.Leg, Group.Relative.Rear, Group.Relative.Right, Group.Relative.Upper) | ALL(ID.Leg, Group.Relative.Rear, Group.Relative.Right, Group.Relative.Lower) |
| ALL(ID.Leg, Group.Relative.Front, Group.Relative.Left, Group.Relative.Lower) | ALL(ID.Leg, Group.Relative.Front, Group.Relative.Left, Group.Relative.Upper) |
| ALL(ID.Leg, Group.Relative.Front, Group.Relative.Right, Group.Relative.Lower) | ALL(ID.Leg, Group.Relative.Front, Group.Relative.Right, Group.Relative.Upper) |
| ALL(ID.Leg, Group.Relative.Left, Group.Relative.Rear, Group.Relative.Lower) | ALL(ID.Leg, Group.Relative.Left, Group.Relative.Rear, Group.Relative.Upper) |
| ALL(ID.Leg, Group.Relative.Rear, Group.Relative.Right, Group.Relative.Lower) | ALL(ID.Leg, Group.Relative.Rear, Group.Relative.Right, Group.Relative.Upper) |
| ANY(ID.Head, ID.Weapon.Shotgun, ID.Weapon.Grenade) | ANY(ID.Weapon.Shotgun, ID.Weapon.Grenade, ID.Head) |
| ID.Frame | ID.Head |

</details>
