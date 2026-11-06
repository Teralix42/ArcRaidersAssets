# Canto

[Weapons](README.md) · [Mechanics](Mechanics.md) · [ARC damage model](../ARC/Damage_Model.md)

**Ammo:** Medium · **Game ID:** `SMG_Medium_01`

[Weapon blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_Item_SMG_Medium_01.json) · [Item config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_Medium_01/DA_Item_SMG_Medium_01.json) · [Level modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_WeaponQualitySet_SMG_Medium_01.json) · [Projectile](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_Projectile_SMG_Medium_01.json)

[Timing fields and game-code formulas](Mechanics.md#firing-and-reload-timers).

### Level I

| Stat | Value |
| --- | --- |
| Body damage / projectile | 6.5 |
| Headshot multiplier | 1.75× |
| ARC armor multiplier | 0.8× |
| ARC weak-point multiplier | 1× |
| Configured fire rate (RPM) | 850 |
| RPM interval (s) | 0.0706 |
| Magazine | 18 |
| Reload stat (s) | 4 |
| Firing mode | Full-auto |
| ARC armor propagation multiplier | 0.4× |
| Durability burn rate | 0.001275 |
| Partial-reload base duration (s) | 2.5 |

### Level II–IV changes

All deltas are relative to Level I. A dash means unchanged.

| Level | Magazine | Reload stat (s) | Durability burn rate | Handling modifiers |
| --- | --- | --- | --- | --- |
| II | +2 | −0.5 | −0.000127 | −13.043478% max firing dispersion |
| III | +4 | −1 | −0.000255 | −26.086957% max firing dispersion |
| IV | +6 | −1.5 | −0.000383 | −39.130435% max firing dispersion |

### Amplified

Default changes are relative to Level IV; upgrade changes are relative to the Amplified default. Prerequisite changes are included where required.

| Upgrade | Stat changes | What it does | Game files |
| --- | --- | --- | --- |
| Default | Durability burn rate **−0.000446** | Amplified baseline. | [Amplified Durability](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Upgrades/DA_Upgrade_SMG_Medium_01_Ascended.json) · [Amplified blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/BP_Item_SMG_Medium_01_Ascended.json) |
| Carbine Conversion | Configured fire rate (RPM) **−85**, −20% base dispersion, −20% dispersion gained per shot, −28.571429% max firing dispersion, −50% ADS recoil gain, +0.2 equip time (s), +0.2 unequip time (s), RPM interval **+0.0078 s (0.0706 → 0.0784 s)** | Repurposes the Canto as a carbine, greatly improving stability and accuracy at the cost of agility. | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Upgrades/DA_Upgrade_SMG_Medium_01_Carbine.json) · [Modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Upgrades/BP_UpgradeWeaponMod_SMG_Medium_01_Carbine.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Permutations/BP_Item_SMG_Medium_01_Carbine.json) |
| Incendiary Rounds | Burn **+0.5 thermal / 0.1 s tick**, **2 s** duration, **1** stack maximum | Adds an incendiary compound to the projectile, setting targets on fire when hit. 0.5 thermal damage every 0.1 s for 2 s, up to 1 stack. | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Upgrades/DA_Upgrade_SMG_Medium_01_IncendiaryRounds.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Permutations/BP_Item_SMG_Medium_01_IncendiaryRounds.json) · [Projectile](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/BP_Projectile_SMG_Medium_Incendiary.json) · [Burning effect](../Sources/PioneerGame/Content/Pioneer/Core/Gameplay/StatusEffects/GE_Burning_Small.json) |
| Sprint Shooting | Firing while sprinting **enabled** | Ergonomic fittings that allow the weapon to be comfortably fired while sprinting. | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Upgrades/DA_Upgrade_SMG_Medium_01_SprintShooting.json) · [Modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Upgrades/BP_UpgradeWeaponMod_SMG_Medium_01_SprintShooting.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Permutations/BP_Item_SMG_Medium_01_SprintShooting.json) |

**Mutually exclusive:** Carbine Conversion, Sprint Shooting.

### Direct physical damage to ARC

Baseline damage per projectile at full exposure, before falloff and damage propagation. [ARC damage model](../ARC/Damage_Model.md)

| Part group | Damage |
| --- | --- |
| Normal | 6.5 |
| Armor | 2.08 |
| Sturdy | 2.6 |
| WeakPoint | 9.75 |
| Critical | 9.75 |
| Fragile | 7.8 |

### Damage falloff

| Distance (m) | Damage factor | Interpolation |
| --- | --- | --- |
| 0 | 1.001× | Linear |
| 150 | 1.001× | Linear |
| 170 | 0.6× | Linear |

[Game curve](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_Medium_01/Curve_DamageFalloff_SMG_Medium_01.json)
