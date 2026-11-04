# Frigate Cannon

[ARC stats](README.md) · [Damage model](Damage_Model.md)

**Configured frame rule:** 999999 HP. **Internal class:** `C_Rose`.

Frame HP is assigned separately from part HP. A dash marks an unknown or unassigned value.

[Balancing and part HP](../Sources/PioneerGame/Content/Pioneer/Enemies/Turret/Rose/DataAssets/DA_Balancing_C_Rose.json) · [Enemy type](../Sources/PioneerGame/Content/Pioneer/Enemies/Turret/Rose/DataAssets/DA_EnemyType_Rose.json)

<details>
<summary>More game files</summary>

- [CSSC_Rose.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Turret/Rose/Art/CSSC_Rose.json)
- [C_Rose.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Turret/Rose/C_Rose.json)
- [DA_EnemyMetaData_Rose.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Turret/Rose/DataAssets/DA_EnemyMetaData_Rose.json)

</details>


### Weak and critical parts

No explicit WeakPoint/Critical resistance assignment was recovered for this profile. This does not imply invulnerability.

### Outgoing damage rules

Configured values keyed by the part or attack tag. Attack timing and the final damage against a Raider depend on the attack and target.

| Tag | Damage type | Configured damage |
| --- | --- | --- |
| ID.Eye | Explosive | 75 |

### Every named part

This list includes mesh records such as sockets and proxies. See the [damage model](Damage_Model.md) for how weapon multipliers apply to each resistance group.

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
