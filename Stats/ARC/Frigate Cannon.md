# Frigate Cannon

[ARC stats](README.md) · [Machine-readable data](arc_parts.json) · [Damage model](Damage_Model.md)

**Configured frame rule:** 999999 HP. **Internal class:** `C_Rose`.

Frame HP is a balancing rule, not the sum of every limb or plate. Part rules and damage propagation are separate. `—` means unknown or unassigned.


### Weak and critical parts

No explicit WeakPoint/Critical resistance assignment was recovered for this profile. This does not imply invulnerability.

### Every named part

These records also include sockets, bones, and proxy components; they are not all independent damageable hitboxes. The weapon’s separate ARC armor and weak-point multipliers still apply where indicated in JSON.

| Part | Configured HP | Resistance group | Physical damage × | Health rules |
| --- | --- | --- | --- | --- |
| Barrel_L_Muzzle | 999999 | — | — | 2, 4 |
| Barrel_R_Muzzle | 999999 | — | — | 2, 4 |
| Main | 999999 | Armor | 0.4 | 0 |
| Gimbal | 999999 | Armor | 0.4 | 3 |
| AmmoCase | 999999 | Armor | 0.4 | 5 |
| Sensor | 999999 | Armor | 0.4 | 5 |
| Receiver | 999999 | Armor | 0.4 | 1 |
| Barrel_L | 999999 | Armor | 0.4 | 4 |
| Barrel_R | 999999 | Armor | 0.4 | 4 |

### Exact health assignment rules

| Rule | Tag query | HP | Matched parts |
| --- | --- | --- | --- |
| 0 | ID.Frame | 999999 | Main |
| 1 | ID.Arm | 999999 | Receiver |
| 2 | Muzzle | 999999 | Barrel_L_Muzzle, Barrel_R_Muzzle |
| 3 | ID.Joint | 999999 | Gimbal |
| 4 | ID.Weapon | 999999 | Barrel_L_Muzzle, Barrel_R_Muzzle, Barrel_L, Barrel_R |
| 5 | ANY(ID.Vent, ID.Sensor) | 999999 | AmmoCase, Sensor |

Some actor/style sources have partial-decoding warnings; the balancing health tables parsed separately. The JSON retains the warnings and recovered destruction settings.

<details>
<summary>Actual game source files</summary>

- [Content/Pioneer/Enemies/Turret/Rose/Art/CSSC_Rose.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Turret/Rose/Art/CSSC_Rose.json)
- [Content/Pioneer/Enemies/Turret/Rose/C_Rose.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Turret/Rose/C_Rose.json)
- [Content/Pioneer/Enemies/Turret/Rose/DataAssets/DA_Balancing_C_Rose.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Turret/Rose/DataAssets/DA_Balancing_C_Rose.json)
- [Content/Pioneer/Enemies/Turret/Rose/DataAssets/DA_EnemyMetaData_Rose.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Turret/Rose/DataAssets/DA_EnemyMetaData_Rose.json)
- [Content/Pioneer/Enemies/Turret/Rose/DataAssets/DA_EnemyType_Rose.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Turret/Rose/DataAssets/DA_EnemyType_Rose.json)

</details>
