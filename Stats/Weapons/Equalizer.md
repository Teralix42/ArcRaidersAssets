# Equalizer

[Weapons](README.md) · [Mechanics](Mechanics.md) · [ARC damage model](../ARC/Damage_Model.md)

**Ammo:** Energy · **Game ID:** `Special_BeamRifle_01`

[Weapon blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_BeamRifle_01/BP_Item_Special_BeamRifle_01.json) · [Item config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_BeamRifle_01/DA_Item_Special_BeamRifle_01.json) · [Projectile](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_BeamRifle_01/BP_Projectile_Special_BeamRifle_01.json)

[Timing fields and game-code formulas](Mechanics.md#firing-and-reload-timers).

### Standard

| Stat | Value |
| --- | --- |
| Body damage / projectile | 8 |
| Headshot multiplier | 2× |
| ARC armor multiplier | 2.5× |
| ARC weak-point multiplier | 1.5× |
| Configured fire rate (RPM) | 500 |
| RPM interval (s) | 0.12 |
| Magazine | 50 |
| Reload stat (s) | 3 |
| Firing mode | Full-auto |
| ARC armor propagation multiplier | 1× |
| Durability burn rate | 0.000299 |
| Partial-reload base duration (s) | 3 |

### Firing, reload and impact details

- Initial charge delay (s) **1**
- Charge gained per hit **0.1**
- Charge lost per second **0.1**

### Amplified

Default changes are relative to Standard; upgrade changes are relative to the Amplified default. Prerequisite changes are included where required.

| Upgrade | Stat changes | What it does | Game files |
| --- | --- | --- | --- |
| Default | Durability burn rate **−0.000149** | Amplified baseline. | [Amplified Durability](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/DA_Upgrade_Special_BeamRifle_01_Ascended.json) · [Amplified blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/BP_Item_Special_BeamRifle_01_Ascended.json) |
| Anti-Weak Point | ARC armor multiplier **−1.5×**, ARC weak-point multiplier **+1×** | Deals increased damage to ARC weak points, but deals less damage to ARC armor plating. | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/DA_Upgrade_Special_BeamRifle_01_AntiWeakPoint.json) · [Modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Special_BeamRifle_01_AntiWeakPoint.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Permutations/BP_Item_Special_BeamRifle_01_AntiWeakPoint.json) |
| Bigger Mag | Magazine **+30** | Increases the magazine capacity. | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/DA_Upgrade_Special_BeamRifle_01_BiggerMag.json) · [Modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Special_BeamRifle_01_BiggerMag.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Permutations/BP_Item_Special_BeamRifle_01_BiggerMag.json) |
| Ramping Damage | Damage per tick at zero ramp **−1.6 (8 → 6.4)**, Damage per tick at full ramp **+4 (8 → 12)** | Gradually increases the Equalizer's damage while its laser remains in contact with a valid target. Charge-to-damage curve (0 → 0.8, 1 → 1.5) [Curve](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/Curve_DamagePerConsecutiveShot_Special_BeamRifle_01_RampingDamage.json). | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/DA_Upgrade_Special_BeamRifle_01_RampingDamage.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Permutations/BP_Item_Special_BeamRifle_01_RampingDamage.json) |

**Mutually exclusive:** Ramping Damage, Anti-Weak Point.

### Direct physical damage to ARC

Baseline damage per projectile at full exposure, before falloff and damage propagation. [ARC damage model](../ARC/Damage_Model.md)

| Part group | Damage |
| --- | --- |
| Normal | 8 |
| Armor | 8 |
| Sturdy | 3.2 |
| WeakPoint | 18 |
| Critical | 18 |
| Fragile | 9.6 |

### Damage falloff

| Distance (m) | Damage factor | Interpolation |
| --- | --- | --- |
| 0 | 1.2× | Linear |
| 0.02066667 | 1.2× | Linear |
| 5 | 1.2× | Linear |
| 15 | 1× | Linear |
| 100 | 1× | Linear |
| 200 | 0.5× | Linear |

[Game curve](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Curve_DamageFalloff_Special_BeamRifle_01.json)
