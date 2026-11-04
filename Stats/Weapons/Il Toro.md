[Weapon index](README.md) · [Definitions and mechanics](Mechanics.md) · [JSON data](weapons.json)

# Il Toro

Internal weapon id: `Shotgun_PumpAction_01`. Ammo: **ShotgunAmmo**.

### Standard levels

| Level / variant | Damage / projectile | Projectiles | Full spread | Crit × | ARC armour × | ARC weakpoint × | RPM | Magazine | Reload stat, s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I | 7 | 9 | 63 | 1 | 0.5 | 1 | 38.25 | 5 | 2.5 |
| II | 7 | 9 | 63 | 1 | 0.5 | 1 | 45 | 6 | 2.5 |
| III | 7 | 9 | 63 | 1 | 0.5 | 1 | 51.75 | 7 | 2.5 |
| IV | 7 | 9 | 63 | 1 | 0.5 | 1 | 58.5 | 8 | 2.5 |

#### Level I

| Identity | Value |
| --- | --- |
| Id | Shotgun_PumpAction_01_Level1 |
| Level | 1 |
| Level label | I |
| Variant | Standard |
| Quality index | 0 |
| Uses standard level | 1 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 7 |
| Projectiles / simultaneous shot | 9 |
| Physical damage / full spread | 63 |
| Firearm critical/headshot multiplier | 1 |
| ARC armour multiplier | 0.5 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 38.25 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 5 |
| Reload time stat, seconds | 2.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.007378 |
| Base partial-reload duration, seconds | — |
| Uses shell/looping reload | Yes |
| Base shell-reload entry, seconds | 1 |
| Base shell-reload loop, seconds | 0.7 |
| Base shell-reload exit, seconds | 0.5 |
| Shells loaded per loop | 1 |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 7 | 63 |
| Armor | 0.6 | 0.4 | 0.5 | 1 | 0.2 | 1.4 | 12.6 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 2.8 | 25.2 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 10.5 | 94.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 10.5 | 94.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 8.4 | 75.6 |

##### Upgrades

None.

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

None.

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 63 |
| Fire rate | 7.5 |
| Range | 17 |
| Stability | 85.483 |
| Agility | 56.2 |
| Stealth | 18 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Curve_DamageFalloff_Shotgun_PumpAction_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 2,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 5,000 | 0.5 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Firerate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.85 |
| Multiply | 1 |

###### Clipsize

| Field | Value |
| --- | --- |
| Add | -1 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/BP_Item_Shotgun_PumpAction_01.json |
| Item | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/DA_Item_Shotgun_PumpAction_01.json |
| Quality set | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/BP_WeaponQualitySet_Shotgun_PumpAction_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/BP_WeaponQualitySet_Shotgun_PumpAction_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/BP_Projectile_Shotgun_PumpAction_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/BP_Item_Shotgun_PumpAction_01.json, Script/PrecompiledScript.Cache

#### Level II

| Identity | Value |
| --- | --- |
| Id | Shotgun_PumpAction_01_Level2 |
| Level | 2 |
| Level label | II |
| Variant | Standard |
| Quality index | 1 |
| Uses standard level | 2 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 7 |
| Projectiles / simultaneous shot | 9 |
| Physical damage / full spread | 63 |
| Firearm critical/headshot multiplier | 1 |
| ARC armour multiplier | 0.5 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 45 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 6 |
| Reload time stat, seconds | 2.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.00664 |
| Base partial-reload duration, seconds | — |
| Uses shell/looping reload | Yes |
| Base shell-reload entry, seconds | 1 |
| Base shell-reload loop, seconds | 0.7 |
| Base shell-reload exit, seconds | 0.5 |
| Shells loaded per loop | 1 |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 7 | 63 |
| Armor | 0.6 | 0.4 | 0.5 | 1 | 0.2 | 1.4 | 12.6 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 2.8 | 25.2 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 10.5 | 94.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 10.5 | 94.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 8.4 | 75.6 |

##### Upgrades

None.

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

None.

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 63 |
| Fire rate | 8 |
| Range | 17 |
| Stability | 81.983 |
| Agility | 59.7 |
| Stealth | 18 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Curve_DamageFalloff_Shotgun_PumpAction_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 2,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 5,000 | 0.5 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.9 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/BP_Item_Shotgun_PumpAction_01.json |
| Item | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/DA_Item_Shotgun_PumpAction_01.json |
| Quality set | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/BP_WeaponQualitySet_Shotgun_PumpAction_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/BP_WeaponQualitySet_Shotgun_PumpAction_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/BP_Projectile_Shotgun_PumpAction_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/BP_Item_Shotgun_PumpAction_01.json, Script/PrecompiledScript.Cache

#### Level III

| Identity | Value |
| --- | --- |
| Id | Shotgun_PumpAction_01_Level3 |
| Level | 3 |
| Level label | III |
| Variant | Standard |
| Quality index | 2 |
| Uses standard level | 3 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 7 |
| Projectiles / simultaneous shot | 9 |
| Physical damage / full spread | 63 |
| Firearm critical/headshot multiplier | 1 |
| ARC armour multiplier | 0.5 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 51.75 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 7 |
| Reload time stat, seconds | 2.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.005902 |
| Base partial-reload duration, seconds | — |
| Uses shell/looping reload | Yes |
| Base shell-reload entry, seconds | 1 |
| Base shell-reload loop, seconds | 0.7 |
| Base shell-reload exit, seconds | 0.5 |
| Shells loaded per loop | 1 |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 7 | 63 |
| Armor | 0.6 | 0.4 | 0.5 | 1 | 0.2 | 1.4 | 12.6 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 2.8 | 25.2 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 10.5 | 94.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 10.5 | 94.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 8.4 | 75.6 |

##### Upgrades

None.

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

None.

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 63 |
| Fire rate | 8.5 |
| Range | 17 |
| Stability | 81.983 |
| Agility | 62.2 |
| Stealth | 18 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Curve_DamageFalloff_Shotgun_PumpAction_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 2,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 5,000 | 0.5 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.8 |
| Multiply | 1 |

###### Firerate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.15 |
| Multiply | 1 |

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 1 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/BP_Item_Shotgun_PumpAction_01.json |
| Item | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/DA_Item_Shotgun_PumpAction_01.json |
| Quality set | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/BP_WeaponQualitySet_Shotgun_PumpAction_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/BP_WeaponQualitySet_Shotgun_PumpAction_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/BP_Projectile_Shotgun_PumpAction_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/BP_Item_Shotgun_PumpAction_01.json, Script/PrecompiledScript.Cache

#### Level IV

| Identity | Value |
| --- | --- |
| Id | Shotgun_PumpAction_01_Level4 |
| Level | 4 |
| Level label | IV |
| Variant | Standard |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 7 |
| Projectiles / simultaneous shot | 9 |
| Physical damage / full spread | 63 |
| Firearm critical/headshot multiplier | 1 |
| ARC armour multiplier | 0.5 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 58.5 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 8 |
| Reload time stat, seconds | 2.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.005165 |
| Base partial-reload duration, seconds | — |
| Uses shell/looping reload | Yes |
| Base shell-reload entry, seconds | 1 |
| Base shell-reload loop, seconds | 0.7 |
| Base shell-reload exit, seconds | 0.5 |
| Shells loaded per loop | 1 |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 7 | 63 |
| Armor | 0.6 | 0.4 | 0.5 | 1 | 0.2 | 1.4 | 12.6 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 2.8 | 25.2 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 10.5 | 94.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 10.5 | 94.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 8.4 | 75.6 |

##### Upgrades

None.

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

None.

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 63 |
| Fire rate | 9.5 |
| Range | 17 |
| Stability | 81.983 |
| Agility | 64.7 |
| Stealth | 18 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Curve_DamageFalloff_Shotgun_PumpAction_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 2,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 5,000 | 0.5 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Firerate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.3 |
| Multiply | 1 |

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 2 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/BP_Item_Shotgun_PumpAction_01.json |
| Item | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/DA_Item_Shotgun_PumpAction_01.json |
| Quality set | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/BP_WeaponQualitySet_Shotgun_PumpAction_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/BP_WeaponQualitySet_Shotgun_PumpAction_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/BP_Projectile_Shotgun_PumpAction_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/BP_Item_Shotgun_PumpAction_01.json, Script/PrecompiledScript.Cache

### Amplified configurations

| Level / variant | Damage / projectile | Projectiles | Full spread | Crit × | ARC armour × | ARC weakpoint × | RPM | Magazine | Reload stat, s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Default | 7 | 9 | 63 | 1 | 0.5 | 1 | 58.5 | 8 | 2.5 |
| More Reload | 7 | 9 | 63 | 1 | 0.5 | 1 | 58.5 | 8 | 2.5 |
| More Reload + Slug Rounds | 70 | 1 | 70 | 1 | 1.5 | 1 | 58.5 | 8 | 2.5 |
| Slug Rounds | 70 | 1 | 70 | 1 | 1.5 | 1 | 58.5 | 8 | 2.5 |

#### Amplified — Default

| Identity | Value |
| --- | --- |
| Id | Shotgun_PumpAction_01_Ascended |
| Level | 5 |
| Level label | Amplified |
| Variant | Default |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 7 |
| Projectiles / simultaneous shot | 9 |
| Physical damage / full spread | 63 |
| Firearm critical/headshot multiplier | 1 |
| ARC armour multiplier | 0.5 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 58.5 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 8 |
| Reload time stat, seconds | 2.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.002582 |
| Base partial-reload duration, seconds | — |
| Uses shell/looping reload | Yes |
| Base shell-reload entry, seconds | 1 |
| Base shell-reload loop, seconds | 0.7 |
| Base shell-reload exit, seconds | 0.5 |
| Shells loaded per loop | 1 |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 7 | 63 |
| Armor | 0.6 | 0.4 | 0.5 | 1 | 0.2 | 1.4 | 12.6 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 2.8 | 25.2 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 10.5 | 94.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 10.5 | 94.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 8.4 | 75.6 |

##### Upgrades

None.

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

None.

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 63 |
| Fire rate | 9.5 |
| Range | 17 |
| Stability | 81.983 |
| Agility | 64.7 |
| Stealth | 18 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Curve_DamageFalloff_Shotgun_PumpAction_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 2,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 5,000 | 0.5 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Firerate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.3 |
| Multiply | 1 |

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 2 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/BP_Item_Shotgun_PumpAction_01_Ascended.json |
| Item | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/DA_Item_Shotgun_PumpAction_01_Ascended.json |
| Quality set | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/BP_WeaponQualitySet_Shotgun_PumpAction_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/BP_WeaponQualitySet_Shotgun_PumpAction_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/BP_Projectile_Shotgun_PumpAction_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/BP_Item_Shotgun_PumpAction_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | Shotgun_PumpAction_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Upgrades/DA_Upgrade_Shotgun_PumpAction_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — More Reload

| Identity | Value |
| --- | --- |
| Id | Shotgun_PumpAction_01_MoreReload |
| Level | 5 |
| Level label | Amplified |
| Variant | More Reload |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 7 |
| Projectiles / simultaneous shot | 9 |
| Physical damage / full spread | 63 |
| Firearm critical/headshot multiplier | 1 |
| ARC armour multiplier | 0.5 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 58.5 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 8 |
| Reload time stat, seconds | 2.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.002582 |
| Base partial-reload duration, seconds | — |
| Uses shell/looping reload | Yes |
| Base shell-reload entry, seconds | 1 |
| Base shell-reload loop, seconds | 0.7 |
| Base shell-reload exit, seconds | 0.5 |
| Shells loaded per loop | 2 |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 7 | 63 |
| Armor | 0.6 | 0.4 | 0.5 | 1 | 0.2 | 1.4 | 12.6 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 2.8 | 25.2 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 10.5 | 94.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 10.5 | 94.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 8.4 | 75.6 |

##### Upgrades

###### More Reload

| Field | Value |
| --- | --- |
| Id | Shotgun_PumpAction_01_MoreReload |
| Name | More Reload |
| Description | Increases the number of bullets loaded at a time, reducing reload time. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Upgrades/DA_Upgrade_Shotgun_PumpAction_01_MoreReload.json |
| Modifier source path | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Shotgun_PumpAction_01_MoreReload.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Shotgun_PumpAction_01_MoreReload.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Loopingreloadamount**

| Field | Value |
| --- | --- |
| Add | 1 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

None.

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 63 |
| Fire rate | 9.5 |
| Range | 17 |
| Stability | 81.983 |
| Agility | 64.7 |
| Stealth | 18 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Curve_DamageFalloff_Shotgun_PumpAction_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 2,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 5,000 | 0.5 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Firerate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.3 |
| Multiply | 1 |

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 2 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Loopingreloadamount

| Field | Value |
| --- | --- |
| Add | 1 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Permutations/BP_Item_Shotgun_PumpAction_01_MoreReload.json |
| Item | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Permutations/DA_Item_Shotgun_PumpAction_01_MoreReload.json |
| Quality set | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/BP_WeaponQualitySet_Shotgun_PumpAction_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/BP_WeaponQualitySet_Shotgun_PumpAction_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/BP_Projectile_Shotgun_PumpAction_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/BP_Item_Shotgun_PumpAction_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | Shotgun_PumpAction_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Upgrades/DA_Upgrade_Shotgun_PumpAction_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — More Reload + Slug Rounds

| Identity | Value |
| --- | --- |
| Id | Shotgun_PumpAction_01_MoreReload_SlugRounds |
| Level | 5 |
| Level label | Amplified |
| Variant | More Reload + Slug Rounds |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 70 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 70 |
| Firearm critical/headshot multiplier | 1 |
| ARC armour multiplier | 1.5 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 58.5 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 8 |
| Reload time stat, seconds | 2.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.002582 |
| Base partial-reload duration, seconds | — |
| Uses shell/looping reload | Yes |
| Base shell-reload entry, seconds | 1 |
| Base shell-reload loop, seconds | 0.7 |
| Base shell-reload exit, seconds | 0.5 |
| Shells loaded per loop | 2 |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 70 | 70 |
| Armor | 0.6 | 0.4 | 1.5 | 1 | 0.6 | 42 | 42 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 28 | 28 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 105 | 105 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 105 | 105 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 84 | 84 |

##### Upgrades

###### More Reload

| Field | Value |
| --- | --- |
| Id | Shotgun_PumpAction_01_MoreReload |
| Name | More Reload |
| Description | Increases the number of bullets loaded at a time, reducing reload time. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Upgrades/DA_Upgrade_Shotgun_PumpAction_01_MoreReload.json |
| Modifier source path | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Shotgun_PumpAction_01_MoreReload.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Shotgun_PumpAction_01_MoreReload.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Loopingreloadamount**

| Field | Value |
| --- | --- |
| Add | 1 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Slug Rounds

| Field | Value |
| --- | --- |
| Id | Shotgun_PumpAction_01_SlugRounds |
| Name | Slug Rounds |
| Description | Replaces the normal shotgun shells with a single large projectile that deals massive damage. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Upgrades/DA_Upgrade_Shotgun_PumpAction_01_SlugRounds.json |
| Modifier source path | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Shotgun_PumpAction_01_SlugRounds.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Shotgun_PumpAction_01_SlugRounds.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Physicaldamage**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 10 |
| Multiply | 1 |

**Falloffdistance**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.8 |
| Multiply | 1 |

**Launchspeed**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.5 |
| Multiply | 1 |

**Basedispersion**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.6 |
| Multiply | 1 |

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

None.

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 63 |
| Fire rate | 9.5 |
| Range | 30 |
| Stability | 81.983 |
| Agility | 64.7 |
| Stealth | 18 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Curve_DamageFalloff_Shotgun_PumpAction_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 2,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 5,000 | 0.5 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Firerate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.3 |
| Multiply | 1 |

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 2 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Loopingreloadamount

| Field | Value |
| --- | --- |
| Add | 1 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Physicaldamage

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 10 |
| Multiply | 1 |

###### Falloffdistance

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.8 |
| Multiply | 1 |

###### Launchspeed

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.5 |
| Multiply | 1 |

###### Basedispersion

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.6 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Permutations/BP_Item_Shotgun_PumpAction_01_MoreReload_SlugRounds.json |
| Item | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Permutations/DA_Item_Shotgun_PumpAction_01_MoreReload_SlugRounds.json |
| Quality set | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/BP_WeaponQualitySet_Shotgun_PumpAction_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/BP_WeaponQualitySet_Shotgun_PumpAction_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/BP_Projectile_Shotgun_PumpAction_01_SlugRounds.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Permutations/BP_Item_Shotgun_PumpAction_01_MoreReload_SlugRounds.json, Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/BP_Item_Shotgun_PumpAction_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | Shotgun_PumpAction_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Upgrades/DA_Upgrade_Shotgun_PumpAction_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Slug Rounds

| Identity | Value |
| --- | --- |
| Id | Shotgun_PumpAction_01_SlugRounds |
| Level | 5 |
| Level label | Amplified |
| Variant | Slug Rounds |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 70 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 70 |
| Firearm critical/headshot multiplier | 1 |
| ARC armour multiplier | 1.5 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 58.5 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 8 |
| Reload time stat, seconds | 2.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.002582 |
| Base partial-reload duration, seconds | — |
| Uses shell/looping reload | Yes |
| Base shell-reload entry, seconds | 1 |
| Base shell-reload loop, seconds | 0.7 |
| Base shell-reload exit, seconds | 0.5 |
| Shells loaded per loop | 1 |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 70 | 70 |
| Armor | 0.6 | 0.4 | 1.5 | 1 | 0.6 | 42 | 42 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 28 | 28 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 105 | 105 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 105 | 105 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 84 | 84 |

##### Upgrades

###### Slug Rounds

| Field | Value |
| --- | --- |
| Id | Shotgun_PumpAction_01_SlugRounds |
| Name | Slug Rounds |
| Description | Replaces the normal shotgun shells with a single large projectile that deals massive damage. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Upgrades/DA_Upgrade_Shotgun_PumpAction_01_SlugRounds.json |
| Modifier source path | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Shotgun_PumpAction_01_SlugRounds.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Shotgun_PumpAction_01_SlugRounds.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Physicaldamage**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 10 |
| Multiply | 1 |

**Falloffdistance**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.8 |
| Multiply | 1 |

**Launchspeed**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.5 |
| Multiply | 1 |

**Basedispersion**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.6 |
| Multiply | 1 |

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

None.

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 63 |
| Fire rate | 9.5 |
| Range | 30 |
| Stability | 81.983 |
| Agility | 64.7 |
| Stealth | 18 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Curve_DamageFalloff_Shotgun_PumpAction_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 2,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 5,000 | 0.5 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Firerate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.3 |
| Multiply | 1 |

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 2 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Physicaldamage

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 10 |
| Multiply | 1 |

###### Falloffdistance

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.8 |
| Multiply | 1 |

###### Launchspeed

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.5 |
| Multiply | 1 |

###### Basedispersion

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.6 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Permutations/BP_Item_Shotgun_PumpAction_01_SlugRounds.json |
| Item | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Permutations/DA_Item_Shotgun_PumpAction_01_SlugRounds.json |
| Quality set | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/BP_WeaponQualitySet_Shotgun_PumpAction_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/BP_WeaponQualitySet_Shotgun_PumpAction_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/BP_Projectile_Shotgun_PumpAction_01_SlugRounds.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Permutations/BP_Item_Shotgun_PumpAction_01_SlugRounds.json, Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/BP_Item_Shotgun_PumpAction_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | Shotgun_PumpAction_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Upgrades/DA_Upgrade_Shotgun_PumpAction_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

<details>
<summary>Actual game source files</summary>

- [Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/BP_Item_Shotgun_PumpAction_01_Ascended.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/BP_Item_Shotgun_PumpAction_01_Ascended.json)
- [Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/BP_Projectile_Shotgun_PumpAction_01_SlugRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/BP_Projectile_Shotgun_PumpAction_01_SlugRounds.json)
- [Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/DA_Item_Shotgun_PumpAction_01_Ascended.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/DA_Item_Shotgun_PumpAction_01_Ascended.json)
- [Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Permutations/BP_Item_Shotgun_PumpAction_01_MoreReload.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Permutations/BP_Item_Shotgun_PumpAction_01_MoreReload.json)
- [Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Permutations/BP_Item_Shotgun_PumpAction_01_MoreReload_SlugRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Permutations/BP_Item_Shotgun_PumpAction_01_MoreReload_SlugRounds.json)
- [Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Permutations/BP_Item_Shotgun_PumpAction_01_SlugRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Permutations/BP_Item_Shotgun_PumpAction_01_SlugRounds.json)
- [Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Permutations/DA_Item_Shotgun_PumpAction_01_MoreReload.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Permutations/DA_Item_Shotgun_PumpAction_01_MoreReload.json)
- [Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Permutations/DA_Item_Shotgun_PumpAction_01_MoreReload_SlugRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Permutations/DA_Item_Shotgun_PumpAction_01_MoreReload_SlugRounds.json)
- [Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Permutations/DA_Item_Shotgun_PumpAction_01_SlugRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Permutations/DA_Item_Shotgun_PumpAction_01_SlugRounds.json)
- [Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Shotgun_PumpAction_01_MoreReload.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Shotgun_PumpAction_01_MoreReload.json)
- [Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Shotgun_PumpAction_01_SlugRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Shotgun_PumpAction_01_SlugRounds.json)
- [Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Upgrades/DA_Upgrade_Shotgun_PumpAction_01_Ascended.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Upgrades/DA_Upgrade_Shotgun_PumpAction_01_Ascended.json)
- [Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Upgrades/DA_Upgrade_Shotgun_PumpAction_01_MoreReload.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Upgrades/DA_Upgrade_Shotgun_PumpAction_01_MoreReload.json)
- [Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Upgrades/DA_Upgrade_Shotgun_PumpAction_01_SlugRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Upgrades/DA_Upgrade_Shotgun_PumpAction_01_SlugRounds.json)
- [Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/BP_Item_Shotgun_PumpAction_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/BP_Item_Shotgun_PumpAction_01.json)
- [Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/BP_Projectile_Shotgun_PumpAction_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/BP_Projectile_Shotgun_PumpAction_01.json)
- [Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/BP_WeaponQualitySet_Shotgun_PumpAction_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/BP_WeaponQualitySet_Shotgun_PumpAction_01.json)
- [Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Curve_DamageFalloff_Shotgun_PumpAction_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Curve_DamageFalloff_Shotgun_PumpAction_01.json)
- [Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/DA_Item_Shotgun_PumpAction_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/DA_Item_Shotgun_PumpAction_01.json)

</details>
