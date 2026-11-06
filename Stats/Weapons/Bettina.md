# Bettina

[Weapons](README.md) · [Mechanics](Mechanics.md) · [ARC damage model](../ARC/Damage_Model.md)

**Ammo:** Heavy · **Game ID:** `AssaultRifle_Heavy_01`

[Weapon blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_Item_AssaultRifle_Heavy_01.json) · [Item config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/DA_Item_AssaultRifle_Heavy_01.json) · [Level modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_WeaponQualitySet_AssaultRifle_Heavy_01.json) · [Projectile](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_Projectile_AssaultRifle_Heavy_01.json)

[Timing fields and game-code formulas](Mechanics.md#firing-and-reload-timers).

### Level I

| Stat | Value |
| --- | --- |
| Body damage / projectile | 16 |
| Headshot multiplier | 2× |
| ARC armor multiplier | 2× |
| ARC weak-point multiplier | 1× |
| Configured fire rate (RPM) | 270 |
| RPM interval (s) | 0.2222 |
| Magazine | 22 |
| Reload stat (s) | 4.5 |
| Firing mode | Full-auto |
| ARC armor propagation multiplier | 1× |
| Durability burn rate | 0.001317 |
| Partial-reload base duration (s) | 3.2 |

### Level II–IV changes

All deltas are relative to Level I. A dash means unchanged.

| Level | Configured fire rate (RPM) | Reload stat (s) | Durability burn rate | RPM interval (s) |
| --- | --- | --- | --- | --- |
| II | +15 | −0.5 | −0.000132 | −0.0117 |
| III | +30 | −1 | −0.000263 | −0.0222 |
| IV | +45 | −1.5 | −0.000395 | −0.0317 |

### Amplified

Default changes are relative to Level IV; upgrade changes are relative to the Amplified default. Prerequisite changes are included where required.

| Upgrade | Stat changes | What it does | Game files |
| --- | --- | --- | --- |
| Default | Durability burn rate **−0.000461**, Input-buffer window **+0.09 s (0.01 → 0.1 s)** | Amplified baseline. | [Amplified Durability](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_Heavy_01_Ascended.json) · [Amplified blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/BP_Item_AssaultRifle_Heavy_01_Ascended.json) |
| Bigger Mag | Magazine **+15** | Increases the magazine capacity. | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_Heavy_01_BiggerMag.json) · [Modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_Heavy_01_BiggerMag.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Permutations/BP_Item_AssaultRifle_Heavy_01_BiggerMag.json) |
| Semi-Auto | Body damage / projectile **+3**, Firing mode **Semi-auto**, +80% dispersion gained per shot, −20% max firing dispersion, +100% dispersion recovery speed, +20% recoil recovery time, Fire-rate percentage modifier **−20%** | Makes the weapon semi-automatic. | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_Heavy_01_SemiAuto.json) · [Modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_Heavy_01_SingleFire.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Permutations/BP_Item_AssaultRifle_Heavy_01_SemiAuto.json) |
| X-Rounds (requires Semi-Auto) | Body damage / projectile **+6**, ARC armor multiplier **+0.5×**, Magazine **−4**, Firing mode **Semi-auto**, +20% vertical recoil, +20% horizontal recoil, −40% projectile speed, +80% dispersion gained per shot, −20% max firing dispersion, +100% dispersion recovery speed, +20% recoil recovery time, Fire-rate percentage modifier **−20%** | Adds an explosive compound to the projectile, dealing slightly increased damage to Raiders and significantly increased damage to ARC Armor plating. | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_Heavy_01_XRounds.json) · [Modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_Heavy_01_XRounds.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Permutations/BP_Item_AssaultRifle_Heavy_01_SemiAuto_XRounds.json) |

**Mutually exclusive:** Bigger Mag, Semi-Auto.

### Direct physical damage to ARC

Baseline damage per projectile at full exposure, before falloff and damage propagation. [ARC damage model](../ARC/Damage_Model.md)

| Part group | Damage |
| --- | --- |
| Normal | 16 |
| Armor | 12.8 |
| Sturdy | 6.4 |
| WeakPoint | 24 |
| Critical | 24 |
| Fragile | 19.2 |

### Damage falloff

| Distance (m) | Damage factor | Interpolation |
| --- | --- | --- |
| 0 | 1.0001× | Linear |
| 15 | 1.001× | Linear |
| 180 | 1.001× | Linear |
| 200 | 0.6× | Linear |

[Game curve](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Curve_DamageFalloff_AssaultRifle_Heavy_01.json)
