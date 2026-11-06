# Hairpin

[Weapons](README.md) · [Mechanics](Mechanics.md) · [ARC damage model](../ARC/Damage_Model.md)

**Ammo:** Light · **Game ID:** `Pistol_Silenced_01`

[Weapon blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_Item_Pistol_Silenced_01.json) · [Item config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_Silenced_01/DA_Item_Pistol_Silenced_01.json) · [Level modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_WeaponQualitySet_Pistol_Silenced_01.json) · [Projectile](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_Projectile_Pistol_Silenced_01.json) · [BP_Item_Pistol_Base](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shared/BaseClasses/Pistol_Base/BP_Item_Pistol_Base.json)

[Timing fields and game-code formulas](Mechanics.md#firing-and-reload-timers).

### Level I

| Stat | Value |
| --- | --- |
| Body damage / projectile | 20 |
| Headshot multiplier | 2.5× |
| ARC armor multiplier | 0.2× |
| ARC weak-point multiplier | 1× |
| Configured fire rate (RPM) | 55.5 |
| RPM interval (s) | 1.0811 |
| Magazine | 8 |
| Input-buffer window (s) | 0.01 |
| Reload stat (s) | 3 |
| Firing mode | Semi-auto |
| ARC armor propagation multiplier | 0.1× |
| Durability burn rate | 0.003673 |
| Partial-reload base duration (s) | 1.4 |

### Level II–IV changes

All deltas are relative to Level I. A dash means unchanged.

| Level | Configured fire rate (RPM) | Reload stat (s) | Durability burn rate | RPM interval (s) |
| --- | --- | --- | --- | --- |
| II | +4.5 | −0.5 | −0.000367 | −0.0811 |
| III | +9 | −1 | −0.000735 | −0.1508 |
| IV | +13.5 | −1.5 | −0.001102 | −0.2115 |

### Amplified

Default changes are relative to Level IV; upgrade changes are relative to the Amplified default. Prerequisite changes are included where required.

| Upgrade | Stat changes | What it does | Game files |
| --- | --- | --- | --- |
| Default | Durability burn rate **−0.001285**, Input-buffer window **+0.19 s (0.01 → 0.2 s)** | Amplified baseline. | [Amplified Durability](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Upgrades/DA_Upgrade_Pistol_Silenced_01_Ascended.json) · [Amplified blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/BP_Item_Pistol_Silenced_01_Ascended.json) |
| Incendiary Rounds | Burn **+0.5 thermal / 0.1 s tick**, **2 s** duration, **1** stack maximum | Adds an incendiary compound to the projectile, setting targets on fire when hit. 0.5 thermal damage every 0.1 s for 2 s, up to 1 stack. | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Upgrades/DA_Upgrade_Pistol_Silenced_01_IncendiaryRounds.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Permutations/BP_Item_Pistol_Silenced_01_IncendiaryRounds.json) · [Projectile](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/BP_Projectile_Pistol_Silenced_Incendiary.json) · [Burning effect](../Sources/PioneerGame/Content/Pioneer/Core/Gameplay/StatusEffects/GE_Burning_Small.json) |
| Semi-Auto | Headshot multiplier **−0.5×**, +0.4 dispersion gained per shot, +10 max firing dispersion, Fire-rate percentage modifier **+150%** | Makes the weapon semi-automatic. | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Upgrades/DA_Upgrade_Pistol_Silenced_01_SemiAuto.json) · [Modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_Silenced_01_SemiAuto.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Permutations/BP_Item_Pistol_Silenced_01_SemiAuto.json) |
| Tracker Rounds | +5 tracking duration (s) | Replaces the bullets with tracker rounds that briefly reveal the position of targets they hit. | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Upgrades/DA_Upgrade_Pistol_Silenced_01_TrackerRounds.json) · [Modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_Silenced_01_TrackerRounds.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Permutations/BP_Item_Pistol_Silenced_01_TrackerRounds.json) |
| Sprint Shooting (requires Semi-Auto) | Headshot multiplier **−0.5×**, +0.4 dispersion gained per shot, +10 max firing dispersion, Firing while sprinting **enabled**, Fire-rate percentage modifier **+150%** | Ergonomic fittings that allow the weapon to be comfortably fired while sprinting. | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Upgrades/DA_Upgrade_Pistol_Silenced_01_SprintShooting.json) · [Modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_Silenced_01_SprintShooting.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Permutations/BP_Item_Pistol_Silenced_01_SemiAuto_SprintShooting.json) |

**Mutually exclusive:** Semi-Auto, Tracker Rounds, Incendiary Rounds.

### Direct physical damage to ARC

Baseline damage per projectile at full exposure, before falloff and damage propagation. [ARC damage model](../ARC/Damage_Model.md)

| Part group | Damage |
| --- | --- |
| Normal | 20 |
| Armor | 1.6 |
| Sturdy | 8 |
| WeakPoint | 30 |
| Critical | 30 |
| Fragile | 24 |

### Damage falloff

| Distance (m) | Damage factor | Interpolation |
| --- | --- | --- |
| 0 | 1.2× | Linear |
| 5 | 1.2× | Linear |
| 15 | 1.001× | Linear |
| 130 | 1.001× | Linear |
| 150 | 0.6× | Linear |

[Game curve](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Curve_DamageFalloff_Pistol_Silenced_01.json)
