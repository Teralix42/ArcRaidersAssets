# Kettle

[Weapons](README.md) · [Mechanics](Mechanics.md) · [ARC damage model](../ARC/Damage_Model.md)

**Ammo:** Light · **Game ID:** `AssaultRifle_Pneumatic_01`

[Weapon blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_Item_AssaultRifle_Pneumatic_01.json) · [Item config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/DA_Item_AssaultRifle_Pneumatic_01.json) · [Level modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_WeaponQualitySet_AssaultRifle_Pneumatic_01.json) · [Projectile](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_Projectile_AssaultRifle_Pneumatic_01.json)

[Timing fields and game-code formulas](Mechanics.md#firing-and-reload-timers).

### Level I

| Stat | Value |
| --- | --- |
| Body damage / projectile | 8.5 |
| Headshot multiplier | 2.5× |
| ARC armor multiplier | 0.2× |
| ARC weak-point multiplier | 1× |
| Configured fire rate (RPM) | 450 |
| RPM interval (s) | 0.1333 |
| Magazine | 20 |
| Input-buffer window (s) | 0.03 |
| Reload stat (s) | 5 |
| Firing mode | Single-shot |
| ARC armor propagation multiplier | 0.1× |
| Durability burn rate | 0.001607 |
| Partial-reload base duration (s) | 4.5 |

### Level II–IV changes

All deltas are relative to Level I. A dash means unchanged.

| Level | Reload stat (s) | Durability burn rate | Handling modifiers |
| --- | --- | --- | --- |
| II | −0.5 | −0.000161 | +8000 projectile speed |
| III | −1 | −0.000321 | +16000 projectile speed |
| IV | −1.5 | −0.000482 | +24000 projectile speed |

### Amplified

Default changes are relative to Level IV; upgrade changes are relative to the Amplified default. Prerequisite changes are included where required.

| Upgrade | Stat changes | What it does | Game files |
| --- | --- | --- | --- |
| Default | Durability burn rate **−0.000563** | Amplified baseline. | [Amplified Durability](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_Pneumatic_01_Ascended.json) · [Amplified blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/BP_Item_AssaultRifle_Pneumatic_01_Ascended.json) |
| Anti-Shield | Body damage / projectile **−2**, +1.5 Raider shield damage bonus | Redistributes damage to prioritize breaking shields faster. | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_Pneumatic_01_AntiShield.json) · [Modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_Pneumatic_01_AntiShield.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Permutations/BP_Item_AssaultRifle_Pneumatic_01_AntiShield.json) |
| Full-Auto | Headshot multiplier **−0.5×**, Configured fire rate (RPM) **+67.5**, Firing mode **Full-auto**, +30% vertical recoil, +30% horizontal recoil, +30% max firing dispersion, RPM interval **−0.0174 s (0.1333 → 0.1159 s)** | Makes the weapon fully automatic, at the cost of accuracy and stability. | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_Pneumatic_01_FullAuto.json) · [Modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_Pneumatic_01_FullAuto.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Permutations/BP_Item_AssaultRifle_Pneumatic_01_FullAuto.json) |
| X-Rounds | Body damage / projectile **+6.5**, ARC armor multiplier **+0.8×**, Configured fire rate (RPM) **−90**, Magazine **−4**, +15% vertical recoil, +15% horizontal recoil, −30% projectile speed, RPM interval **+0.0333 s (0.1333 → 0.1667 s)** | Adds an explosive compound to the projectile, dealing slightly increased damage to Raiders and significantly increased damage to ARC Armor plating. | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_Pneumatic_01_XRounds.json) · [Modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_Pneumatic_01_XRounds.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Permutations/BP_Item_AssaultRifle_Pneumatic_01_XRounds.json) |

**Mutually exclusive:** X-Rounds, Anti-Shield.

**Mutually exclusive:** X-Rounds, Full-Auto.

### Direct physical damage to ARC

Baseline damage per projectile at full exposure, before falloff and damage propagation. [ARC damage model](../ARC/Damage_Model.md)

| Part group | Damage |
| --- | --- |
| Normal | 8.5 |
| Armor | 0.68 |
| Sturdy | 3.4 |
| WeakPoint | 12.75 |
| Critical | 12.75 |
| Fragile | 10.2 |

### Damage falloff

| Distance (m) | Damage factor | Interpolation |
| --- | --- | --- |
| 0 | 1.2× | Linear |
| 5 | 1.2× | Linear |
| 15 | 1.001× | Linear |
| 130 | 1.001× | Linear |
| 150 | 0.6× | Linear |

[Game curve](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Curve_DamageFalloff_AssaultRifle_Pneumatic_01.json)
