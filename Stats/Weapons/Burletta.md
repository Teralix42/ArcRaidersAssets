[Weapon index](README.md) · [Definitions and mechanics](Mechanics.md) · [JSON data](weapons.json)

# Burletta

Internal weapon id: `Pistol_01`. Ammo: **LightAmmo**.

### Standard levels

| Level / variant | Damage / projectile | Projectiles | Full spread | Crit × | ARC armour × | ARC weakpoint × | RPM | Magazine | Reload stat, s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I | 10 | 1 | 10 | 2.5 | 0.2 | 1 | 500 | 12 | 3 |
| II | 10 | 1 | 10 | 2.5 | 0.2 | 1 | 500 | 12 | 2.5 |
| III | 10 | 1 | 10 | 2.5 | 0.2 | 1 | 500 | 12 | 2 |
| IV | 10 | 1 | 10 | 2.5 | 0.2 | 1 | 500 | 12 | 1.5 |

#### Level I

| Identity | Value |
| --- | --- |
| Id | Pistol_01_Level1 |
| Level | 1 |
| Level label | I |
| Variant | Standard |
| Quality index | 0 |
| Uses standard level | 1 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 10 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 10 |
| Firearm critical/headshot multiplier | 2.5 |
| ARC armour multiplier | 0.2 |
| ARC armour propagation coefficient | 0.1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 500 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 12 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.001531 |
| Base partial-reload duration, seconds | 1.4 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 10 | 10 |
| Armor | 0.6 | 0.4 | 0.2 | 1 | 0.08 | 0.8 | 0.8 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 4 | 4 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 15 | 15 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 15 | 15 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 12 | 12 |

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
| Damage | 10 |
| Fire rate | 33.333 |
| Range | 35.532 |
| Stability | 71.689 |
| Agility | 84.391 |
| Stealth | 24 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Pistol_01/Curve_DamageFalloff_Pistol_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 13,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | 0.5 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Pistol_01/BP_Item_Pistol_01.json |
| Item | Content/Pioneer/Items/Firearms/Pistol_01/DA_Item_Pistol_01.json |
| Quality set | Content/Pioneer/Items/Firearms/Pistol_01/BP_WeaponQualitySet_Pistol_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Pistol_01/BP_WeaponQualitySet_Pistol_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Pistol_01/BP_Projectile_Pistol_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Pistol_01/BP_Item_Pistol_01.json, Script/PrecompiledScript.Cache

#### Level II

| Identity | Value |
| --- | --- |
| Id | Pistol_01_Level2 |
| Level | 2 |
| Level label | II |
| Variant | Standard |
| Quality index | 1 |
| Uses standard level | 2 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 10 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 10 |
| Firearm critical/headshot multiplier | 2.5 |
| ARC armour multiplier | 0.2 |
| ARC armour propagation coefficient | 0.1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 500 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 12 |
| Reload time stat, seconds | 2.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.001378 |
| Base partial-reload duration, seconds | 1.4 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 10 | 10 |
| Armor | 0.6 | 0.4 | 0.2 | 1 | 0.08 | 0.8 | 0.8 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 4 | 4 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 15 | 15 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 15 | 15 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 12 | 12 |

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
| Damage | 10 |
| Fire rate | 33.333 |
| Range | 35.532 |
| Stability | 71.689 |
| Agility | 84.391 |
| Stealth | 24 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Pistol_01/Curve_DamageFalloff_Pistol_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 13,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

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
| Weapon | Content/Pioneer/Items/Firearms/Pistol_01/BP_Item_Pistol_01.json |
| Item | Content/Pioneer/Items/Firearms/Pistol_01/DA_Item_Pistol_01.json |
| Quality set | Content/Pioneer/Items/Firearms/Pistol_01/BP_WeaponQualitySet_Pistol_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Pistol_01/BP_WeaponQualitySet_Pistol_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Pistol_01/BP_Projectile_Pistol_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Pistol_01/BP_Item_Pistol_01.json, Script/PrecompiledScript.Cache

#### Level III

| Identity | Value |
| --- | --- |
| Id | Pistol_01_Level3 |
| Level | 3 |
| Level label | III |
| Variant | Standard |
| Quality index | 2 |
| Uses standard level | 3 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 10 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 10 |
| Firearm critical/headshot multiplier | 2.5 |
| ARC armour multiplier | 0.2 |
| ARC armour propagation coefficient | 0.1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 500 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 12 |
| Reload time stat, seconds | 2 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.001225 |
| Base partial-reload duration, seconds | 1.4 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 10 | 10 |
| Armor | 0.6 | 0.4 | 0.2 | 1 | 0.08 | 0.8 | 0.8 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 4 | 4 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 15 | 15 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 15 | 15 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 12 | 12 |

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
| Damage | 10 |
| Fire rate | 33.333 |
| Range | 35.532 |
| Stability | 71.689 |
| Agility | 84.391 |
| Stealth | 24 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Pistol_01/Curve_DamageFalloff_Pistol_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 13,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.8 |
| Multiply | 1 |

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | -0.5 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Pistol_01/BP_Item_Pistol_01.json |
| Item | Content/Pioneer/Items/Firearms/Pistol_01/DA_Item_Pistol_01.json |
| Quality set | Content/Pioneer/Items/Firearms/Pistol_01/BP_WeaponQualitySet_Pistol_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Pistol_01/BP_WeaponQualitySet_Pistol_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Pistol_01/BP_Projectile_Pistol_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Pistol_01/BP_Item_Pistol_01.json, Script/PrecompiledScript.Cache

#### Level IV

| Identity | Value |
| --- | --- |
| Id | Pistol_01_Level4 |
| Level | 4 |
| Level label | IV |
| Variant | Standard |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 10 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 10 |
| Firearm critical/headshot multiplier | 2.5 |
| ARC armour multiplier | 0.2 |
| ARC armour propagation coefficient | 0.1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 500 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 12 |
| Reload time stat, seconds | 1.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.001072 |
| Base partial-reload duration, seconds | 1.4 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 10 | 10 |
| Armor | 0.6 | 0.4 | 0.2 | 1 | 0.08 | 0.8 | 0.8 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 4 | 4 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 15 | 15 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 15 | 15 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 12 | 12 |

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
| Damage | 10 |
| Fire rate | 33.333 |
| Range | 35.532 |
| Stability | 71.689 |
| Agility | 84.391 |
| Stealth | 24 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Pistol_01/Curve_DamageFalloff_Pistol_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 13,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | -1 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Pistol_01/BP_Item_Pistol_01.json |
| Item | Content/Pioneer/Items/Firearms/Pistol_01/DA_Item_Pistol_01.json |
| Quality set | Content/Pioneer/Items/Firearms/Pistol_01/BP_WeaponQualitySet_Pistol_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Pistol_01/BP_WeaponQualitySet_Pistol_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Pistol_01/BP_Projectile_Pistol_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Pistol_01/BP_Item_Pistol_01.json, Script/PrecompiledScript.Cache

### Amplified configurations

| Level / variant | Damage / projectile | Projectiles | Full spread | Crit × | ARC armour × | ARC weakpoint × | RPM | Magazine | Reload stat, s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Default | 10 | 1 | 10 | 2.5 | 0.2 | 1 | 500 | 12 | 1.5 |
| Burst Fire | 10 | 1 | 10 | 2.5 | 0.2 | 1 | 900 | 12 | 1.5 |
| Burst Fire + Increased Burst | 10 | 1 | 10 | 2.5 | 0.2 | 1 | 1,100 | 15 | 1.5 |
| Burst Fire + Increased Burst + Sprint Shooting | 10 | 1 | 10 | 2.5 | 0.2 | 1 | 1,100 | 15 | 1.5 |
| Burst Fire + Sprint Shooting | 10 | 1 | 10 | 2.5 | 0.2 | 1 | 900 | 12 | 1.5 |
| Full-Auto | 8 | 1 | 8 | 1.5 | 0.2 | 1 | 800 | 12 | 1.5 |
| Full-Auto + Sprint Shooting | 8 | 1 | 8 | 1.5 | 0.2 | 1 | 800 | 12 | 1.5 |
| Sprint Shooting | 10 | 1 | 10 | 2.5 | 0.2 | 1 | 500 | 12 | 1.5 |

#### Amplified — Default

| Identity | Value |
| --- | --- |
| Id | Pistol_01_Ascended |
| Level | 5 |
| Level label | Amplified |
| Variant | Default |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 10 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 10 |
| Firearm critical/headshot multiplier | 2.5 |
| ARC armour multiplier | 0.2 |
| ARC armour propagation coefficient | 0.1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 500 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 12 |
| Reload time stat, seconds | 1.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.000536 |
| Base partial-reload duration, seconds | 1.4 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 10 | 10 |
| Armor | 0.6 | 0.4 | 0.2 | 1 | 0.08 | 0.8 | 0.8 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 4 | 4 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 15 | 15 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 15 | 15 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 12 | 12 |

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
| Damage | 10 |
| Fire rate | 33.333 |
| Range | 35.532 |
| Stability | 71.689 |
| Agility | 84.391 |
| Stealth | 24 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Pistol_01/Curve_DamageFalloff_Pistol_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 13,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | -1 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/BP_Item_Pistol_01_Ascended.json |
| Item | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/DA_Item_Pistol_01_Ascended.json |
| Quality set | Content/Pioneer/Items/Firearms/Pistol_01/BP_WeaponQualitySet_Pistol_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Pistol_01/BP_WeaponQualitySet_Pistol_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Pistol_01/BP_Projectile_Pistol_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Pistol_01/BP_Item_Pistol_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | Pistol_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/DA_Upgrade_Pistol_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Burst Fire

| Identity | Value |
| --- | --- |
| Id | Pistol_01_Burst |
| Level | 5 |
| Level label | Amplified |
| Variant | Burst Fire |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 10 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 10 |
| Firearm critical/headshot multiplier | 2.5 |
| ARC armour multiplier | 0.2 |
| ARC armour propagation coefficient | 0.1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 900 |
| Firing mode | burst |
| Burst size stat | 3 |
| Magazine size | 12 |
| Reload time stat, seconds | 1.5 |
| Cooldown time stat, seconds | 0.25 |
| Durability burn rate stat | 0.000536 |
| Base partial-reload duration, seconds | 1.4 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 10 | 10 |
| Armor | 0.6 | 0.4 | 0.2 | 1 | 0.08 | 0.8 | 0.8 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 4 | 4 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 15 | 15 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 15 | 15 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 12 | 12 |

##### Upgrades

###### Burst Fire

| Field | Value |
| --- | --- |
| Id | Pistol_01_Burst |
| Name | Burst Fire |
| Description | Makes the weapon fire in a burst. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/DA_Upgrade_Pistol_01_Burst.json |
| Modifier source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_01_Burst.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_01_Burst.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Firingmodeoverride**

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Currentfiringmode | EFiringMode::burst |

**Firerate**

| Field | Value |
| --- | --- |
| Add | 400 |
| Addmultiply | 1 |
| Multiply | 1 |

**Burstsize**

| Field | Value |
| --- | --- |
| Add | 2 |
| Addmultiply | 1 |
| Multiply | 1 |

**Cooldowntime**

| Field | Value |
| --- | --- |
| Add | 0.25 |
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
| Damage | 10 |
| Fire rate | 35 |
| Range | 35.532 |
| Stability | 59.048 |
| Agility | 84.391 |
| Stealth | 24 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Pistol_01/Curve_DamageFalloff_Pistol_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 13,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | -1 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Firingmodeoverride

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Currentfiringmode | EFiringMode::burst |

###### Firerate

| Field | Value |
| --- | --- |
| Add | 400 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Burstsize

| Field | Value |
| --- | --- |
| Add | 2 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Cooldowntime

| Field | Value |
| --- | --- |
| Add | 0.25 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/BP_Item_Pistol_01_Burst.json |
| Item | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/DA_Item_Pistol_01_Burst.json |
| Quality set | Content/Pioneer/Items/Firearms/Pistol_01/BP_WeaponQualitySet_Pistol_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Pistol_01/BP_WeaponQualitySet_Pistol_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Pistol_01/BP_Projectile_Pistol_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Pistol_01/BP_Item_Pistol_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | Pistol_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/DA_Upgrade_Pistol_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Burst Fire + Increased Burst

| Identity | Value |
| --- | --- |
| Id | Pistol_01_Burst_IncreasedBurst |
| Level | 5 |
| Level label | Amplified |
| Variant | Burst Fire + Increased Burst |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 10 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 10 |
| Firearm critical/headshot multiplier | 2.5 |
| ARC armour multiplier | 0.2 |
| ARC armour propagation coefficient | 0.1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 1,100 |
| Firing mode | burst |
| Burst size stat | 5 |
| Magazine size | 15 |
| Reload time stat, seconds | 1.5 |
| Cooldown time stat, seconds | 0.25 |
| Durability burn rate stat | 0.000536 |
| Base partial-reload duration, seconds | 1.4 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 10 | 10 |
| Armor | 0.6 | 0.4 | 0.2 | 1 | 0.08 | 0.8 | 0.8 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 4 | 4 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 15 | 15 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 15 | 15 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 12 | 12 |

##### Upgrades

###### Burst Fire

| Field | Value |
| --- | --- |
| Id | Pistol_01_Burst |
| Name | Burst Fire |
| Description | Makes the weapon fire in a burst. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/DA_Upgrade_Pistol_01_Burst.json |
| Modifier source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_01_Burst.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_01_Burst.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Firingmodeoverride**

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Currentfiringmode | EFiringMode::burst |

**Firerate**

| Field | Value |
| --- | --- |
| Add | 400 |
| Addmultiply | 1 |
| Multiply | 1 |

**Burstsize**

| Field | Value |
| --- | --- |
| Add | 2 |
| Addmultiply | 1 |
| Multiply | 1 |

**Cooldowntime**

| Field | Value |
| --- | --- |
| Add | 0.25 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Increased Burst

| Field | Value |
| --- | --- |
| Id | Pistol_01_IncreasedBurst |
| Name | Increased Burst |
| Description | Increases the number of projectiles fired within a burst. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/DA_Upgrade_Pistol_01_IncreasedBurst.json |
| Modifier source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_01_IncreasedBurst.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_01_IncreasedBurst.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Firerate**

| Field | Value |
| --- | --- |
| Add | 200 |
| Addmultiply | 1 |
| Multiply | 1 |

**Burstsize**

| Field | Value |
| --- | --- |
| Add | 2 |
| Addmultiply | 1 |
| Multiply | 1 |

**Clipsize**

| Field | Value |
| --- | --- |
| Add | 3 |
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
| Damage | 10 |
| Fire rate | 42.718 |
| Range | 35.532 |
| Stability | 49.465 |
| Agility | 84.391 |
| Stealth | 24 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Pistol_01/Curve_DamageFalloff_Pistol_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 13,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | -1 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Firingmodeoverride

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Currentfiringmode | EFiringMode::burst |

###### Firerate

| Field | Value |
| --- | --- |
| Add | 600 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Burstsize

| Field | Value |
| --- | --- |
| Add | 4 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Cooldowntime

| Field | Value |
| --- | --- |
| Add | 0.25 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 3 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/BP_Item_Pistol_01_Burst_IncreasedBurst.json |
| Item | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/DA_Item_Pistol_01_Burst_IncreasedBurst.json |
| Quality set | Content/Pioneer/Items/Firearms/Pistol_01/BP_WeaponQualitySet_Pistol_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Pistol_01/BP_WeaponQualitySet_Pistol_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Pistol_01/BP_Projectile_Pistol_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Pistol_01/BP_Item_Pistol_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | Pistol_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/DA_Upgrade_Pistol_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Burst Fire + Increased Burst + Sprint Shooting

| Identity | Value |
| --- | --- |
| Id | Pistol_01_Burst_IncreasedBurst_SprintShooting |
| Level | 5 |
| Level label | Amplified |
| Variant | Burst Fire + Increased Burst + Sprint Shooting |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 10 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 10 |
| Firearm critical/headshot multiplier | 2.5 |
| ARC armour multiplier | 0.2 |
| ARC armour propagation coefficient | 0.1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 1,100 |
| Firing mode | burst |
| Burst size stat | 5 |
| Magazine size | 15 |
| Reload time stat, seconds | 1.5 |
| Cooldown time stat, seconds | 0.25 |
| Durability burn rate stat | 0.000536 |
| Base partial-reload duration, seconds | 1.4 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 10 | 10 |
| Armor | 0.6 | 0.4 | 0.2 | 1 | 0.08 | 0.8 | 0.8 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 4 | 4 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 15 | 15 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 15 | 15 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 12 | 12 |

##### Upgrades

###### Burst Fire

| Field | Value |
| --- | --- |
| Id | Pistol_01_Burst |
| Name | Burst Fire |
| Description | Makes the weapon fire in a burst. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/DA_Upgrade_Pistol_01_Burst.json |
| Modifier source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_01_Burst.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_01_Burst.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Firingmodeoverride**

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Currentfiringmode | EFiringMode::burst |

**Firerate**

| Field | Value |
| --- | --- |
| Add | 400 |
| Addmultiply | 1 |
| Multiply | 1 |

**Burstsize**

| Field | Value |
| --- | --- |
| Add | 2 |
| Addmultiply | 1 |
| Multiply | 1 |

**Cooldowntime**

| Field | Value |
| --- | --- |
| Add | 0.25 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Increased Burst

| Field | Value |
| --- | --- |
| Id | Pistol_01_IncreasedBurst |
| Name | Increased Burst |
| Description | Increases the number of projectiles fired within a burst. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/DA_Upgrade_Pistol_01_IncreasedBurst.json |
| Modifier source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_01_IncreasedBurst.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_01_IncreasedBurst.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Firerate**

| Field | Value |
| --- | --- |
| Add | 200 |
| Addmultiply | 1 |
| Multiply | 1 |

**Burstsize**

| Field | Value |
| --- | --- |
| Add | 2 |
| Addmultiply | 1 |
| Multiply | 1 |

**Clipsize**

| Field | Value |
| --- | --- |
| Add | 3 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Sprint Shooting

| Field | Value |
| --- | --- |
| Id | Pistol_01_SprintShooting |
| Name | Sprint Shooting |
| Description | Ergonomic fittings that allow the weapon to be comfortably fired while sprinting. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/DA_Upgrade_Pistol_01_SprintShooting.json |
| Modifier source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_01_SprintShooting.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_01_SprintShooting.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Blocksprintoverride**

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Bblocksprintduringprimaryuse | No |

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

None.

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 10 |
| Fire rate | 42.718 |
| Range | 35.532 |
| Stability | 49.465 |
| Agility | 89.391 |
| Stealth | 24 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Pistol_01/Curve_DamageFalloff_Pistol_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 13,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | -1 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Firingmodeoverride

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Currentfiringmode | EFiringMode::burst |

###### Firerate

| Field | Value |
| --- | --- |
| Add | 600 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Burstsize

| Field | Value |
| --- | --- |
| Add | 4 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Cooldowntime

| Field | Value |
| --- | --- |
| Add | 0.25 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 3 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Blocksprintoverride

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Bblocksprintduringprimaryuse | No |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/BP_Item_Pistol_01_Burst_IncreasedBurst_SprintShooting.json |
| Item | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/DA_Item_Pistol_01_Burst_IncreasedBurst_SprintShooting.json |
| Quality set | Content/Pioneer/Items/Firearms/Pistol_01/BP_WeaponQualitySet_Pistol_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Pistol_01/BP_WeaponQualitySet_Pistol_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Pistol_01/BP_Projectile_Pistol_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Pistol_01/BP_Item_Pistol_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | Pistol_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/DA_Upgrade_Pistol_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Burst Fire + Sprint Shooting

| Identity | Value |
| --- | --- |
| Id | Pistol_01_Burst_SprintShooting |
| Level | 5 |
| Level label | Amplified |
| Variant | Burst Fire + Sprint Shooting |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 10 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 10 |
| Firearm critical/headshot multiplier | 2.5 |
| ARC armour multiplier | 0.2 |
| ARC armour propagation coefficient | 0.1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 900 |
| Firing mode | burst |
| Burst size stat | 3 |
| Magazine size | 12 |
| Reload time stat, seconds | 1.5 |
| Cooldown time stat, seconds | 0.25 |
| Durability burn rate stat | 0.000536 |
| Base partial-reload duration, seconds | 1.4 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 10 | 10 |
| Armor | 0.6 | 0.4 | 0.2 | 1 | 0.08 | 0.8 | 0.8 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 4 | 4 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 15 | 15 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 15 | 15 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 12 | 12 |

##### Upgrades

###### Burst Fire

| Field | Value |
| --- | --- |
| Id | Pistol_01_Burst |
| Name | Burst Fire |
| Description | Makes the weapon fire in a burst. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/DA_Upgrade_Pistol_01_Burst.json |
| Modifier source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_01_Burst.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_01_Burst.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Firingmodeoverride**

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Currentfiringmode | EFiringMode::burst |

**Firerate**

| Field | Value |
| --- | --- |
| Add | 400 |
| Addmultiply | 1 |
| Multiply | 1 |

**Burstsize**

| Field | Value |
| --- | --- |
| Add | 2 |
| Addmultiply | 1 |
| Multiply | 1 |

**Cooldowntime**

| Field | Value |
| --- | --- |
| Add | 0.25 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Sprint Shooting

| Field | Value |
| --- | --- |
| Id | Pistol_01_SprintShooting |
| Name | Sprint Shooting |
| Description | Ergonomic fittings that allow the weapon to be comfortably fired while sprinting. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/DA_Upgrade_Pistol_01_SprintShooting.json |
| Modifier source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_01_SprintShooting.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_01_SprintShooting.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Blocksprintoverride**

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Bblocksprintduringprimaryuse | No |

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

None.

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 10 |
| Fire rate | 35 |
| Range | 35.532 |
| Stability | 59.048 |
| Agility | 89.391 |
| Stealth | 24 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Pistol_01/Curve_DamageFalloff_Pistol_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 13,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | -1 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Firingmodeoverride

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Currentfiringmode | EFiringMode::burst |

###### Firerate

| Field | Value |
| --- | --- |
| Add | 400 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Burstsize

| Field | Value |
| --- | --- |
| Add | 2 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Cooldowntime

| Field | Value |
| --- | --- |
| Add | 0.25 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Blocksprintoverride

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Bblocksprintduringprimaryuse | No |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/BP_Item_Pistol_01_Burst_SprintShooting.json |
| Item | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/DA_Item_Pistol_01_Burst_SprintShooting.json |
| Quality set | Content/Pioneer/Items/Firearms/Pistol_01/BP_WeaponQualitySet_Pistol_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Pistol_01/BP_WeaponQualitySet_Pistol_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Pistol_01/BP_Projectile_Pistol_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Pistol_01/BP_Item_Pistol_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | Pistol_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/DA_Upgrade_Pistol_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Full-Auto

| Identity | Value |
| --- | --- |
| Id | Pistol_01_FullAuto |
| Level | 5 |
| Level label | Amplified |
| Variant | Full-Auto |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 8 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 8 |
| Firearm critical/headshot multiplier | 1.5 |
| ARC armour multiplier | 0.2 |
| ARC armour propagation coefficient | 0.1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 800 |
| Firing mode | Auto |
| Burst size stat | 1 |
| Magazine size | 12 |
| Reload time stat, seconds | 1.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.000536 |
| Base partial-reload duration, seconds | 1.4 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 8 | 8 |
| Armor | 0.6 | 0.4 | 0.2 | 1 | 0.08 | 0.64 | 0.64 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.2 | 3.2 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 12 | 12 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 12 | 12 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 9.6 | 9.6 |

##### Upgrades

###### Full-Auto

| Field | Value |
| --- | --- |
| Id | Pistol_01_FullAuto |
| Name | Full-Auto |
| Description | Makes the weapon fully automatic, at the cost of accuracy and stability. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/DA_Upgrade_Pistol_01_FullAuto.json |
| Modifier source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_01_FullAuto.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_01_FullAuto.uasset |
| Modifier selection | baked_cache_enabled |

**Modifiers**

**Physicaldamage**

| Field | Value |
| --- | --- |
| Add | -2 |
| Addmultiply | 1 |
| Multiply | 1 |

**Criticaldamagemultiplier**

| Field | Value |
| --- | --- |
| Add | -1 |
| Addmultiply | 1 |
| Multiply | 1 |

**Firerate**

| Field | Value |
| --- | --- |
| Add | 300 |
| Addmultiply | 1 |
| Multiply | 1 |

**Horizontalrecoil**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.5 |
| Multiply | 1 |

**Verticalrecoil**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 2 |
| Multiply | 1 |

**Dispersionrecoveryspeed**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 3 |
| Multiply | 1 |

**Firedispersionmax**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 3 |
| Multiply | 1 |

**Basedispersion**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.5 |
| Multiply | 1 |

**Zoomdispersionscale**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.5 |
| Multiply | 1 |

**Firingmodeoverride**

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Currentfiringmode | EFiringMode::Auto |

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

None.

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 8 |
| Fire rate | 53.333 |
| Range | 35.532 |
| Stability | 41.728 |
| Agility | 80.718 |
| Stealth | 24 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Pistol_01/Curve_DamageFalloff_Pistol_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 13,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | -1 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Physicaldamage

| Field | Value |
| --- | --- |
| Add | -2 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Criticaldamagemultiplier

| Field | Value |
| --- | --- |
| Add | -1 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Firerate

| Field | Value |
| --- | --- |
| Add | 300 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Horizontalrecoil

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.5 |
| Multiply | 1 |

###### Verticalrecoil

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 2 |
| Multiply | 1 |

###### Dispersionrecoveryspeed

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 3 |
| Multiply | 1 |

###### Firedispersionmax

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 3 |
| Multiply | 1 |

###### Basedispersion

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.5 |
| Multiply | 1 |

###### Zoomdispersionscale

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.5 |
| Multiply | 1 |

###### Firingmodeoverride

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Currentfiringmode | EFiringMode::Auto |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/BP_Item_Pistol_01_FullAuto.json |
| Item | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/DA_Item_Pistol_01_FullAuto.json |
| Quality set | Content/Pioneer/Items/Firearms/Pistol_01/BP_WeaponQualitySet_Pistol_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Pistol_01/BP_WeaponQualitySet_Pistol_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Pistol_01/BP_Projectile_Pistol_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Pistol_01/BP_Item_Pistol_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | Pistol_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/DA_Upgrade_Pistol_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Full-Auto + Sprint Shooting

| Identity | Value |
| --- | --- |
| Id | Pistol_01_FullAuto_SprintShooting |
| Level | 5 |
| Level label | Amplified |
| Variant | Full-Auto + Sprint Shooting |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 8 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 8 |
| Firearm critical/headshot multiplier | 1.5 |
| ARC armour multiplier | 0.2 |
| ARC armour propagation coefficient | 0.1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 800 |
| Firing mode | Auto |
| Burst size stat | 1 |
| Magazine size | 12 |
| Reload time stat, seconds | 1.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.000536 |
| Base partial-reload duration, seconds | 1.4 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 8 | 8 |
| Armor | 0.6 | 0.4 | 0.2 | 1 | 0.08 | 0.64 | 0.64 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.2 | 3.2 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 12 | 12 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 12 | 12 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 9.6 | 9.6 |

##### Upgrades

###### Full-Auto

| Field | Value |
| --- | --- |
| Id | Pistol_01_FullAuto |
| Name | Full-Auto |
| Description | Makes the weapon fully automatic, at the cost of accuracy and stability. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/DA_Upgrade_Pistol_01_FullAuto.json |
| Modifier source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_01_FullAuto.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_01_FullAuto.uasset |
| Modifier selection | baked_cache_enabled |

**Modifiers**

**Physicaldamage**

| Field | Value |
| --- | --- |
| Add | -2 |
| Addmultiply | 1 |
| Multiply | 1 |

**Criticaldamagemultiplier**

| Field | Value |
| --- | --- |
| Add | -1 |
| Addmultiply | 1 |
| Multiply | 1 |

**Firerate**

| Field | Value |
| --- | --- |
| Add | 300 |
| Addmultiply | 1 |
| Multiply | 1 |

**Horizontalrecoil**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.5 |
| Multiply | 1 |

**Verticalrecoil**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 2 |
| Multiply | 1 |

**Dispersionrecoveryspeed**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 3 |
| Multiply | 1 |

**Firedispersionmax**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 3 |
| Multiply | 1 |

**Basedispersion**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.5 |
| Multiply | 1 |

**Zoomdispersionscale**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.5 |
| Multiply | 1 |

**Firingmodeoverride**

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Currentfiringmode | EFiringMode::Auto |

###### Sprint Shooting

| Field | Value |
| --- | --- |
| Id | Pistol_01_SprintShooting |
| Name | Sprint Shooting |
| Description | Ergonomic fittings that allow the weapon to be comfortably fired while sprinting. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/DA_Upgrade_Pistol_01_SprintShooting.json |
| Modifier source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_01_SprintShooting.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_01_SprintShooting.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Blocksprintoverride**

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Bblocksprintduringprimaryuse | No |

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

None.

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 8 |
| Fire rate | 53.333 |
| Range | 35.532 |
| Stability | 41.728 |
| Agility | 89.718 |
| Stealth | 24 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Pistol_01/Curve_DamageFalloff_Pistol_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 13,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | -1 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Physicaldamage

| Field | Value |
| --- | --- |
| Add | -2 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Criticaldamagemultiplier

| Field | Value |
| --- | --- |
| Add | -1 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Firerate

| Field | Value |
| --- | --- |
| Add | 300 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Horizontalrecoil

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.5 |
| Multiply | 1 |

###### Verticalrecoil

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 2 |
| Multiply | 1 |

###### Dispersionrecoveryspeed

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 3 |
| Multiply | 1 |

###### Firedispersionmax

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 3 |
| Multiply | 1 |

###### Basedispersion

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.5 |
| Multiply | 1 |

###### Zoomdispersionscale

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.5 |
| Multiply | 1 |

###### Firingmodeoverride

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Currentfiringmode | EFiringMode::Auto |

###### Blocksprintoverride

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Bblocksprintduringprimaryuse | No |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/BP_Item_Pistol_01_FullAuto_SprintShooting.json |
| Item | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/DA_Item_Pistol_01_FullAuto_SprintShooting.json |
| Quality set | Content/Pioneer/Items/Firearms/Pistol_01/BP_WeaponQualitySet_Pistol_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Pistol_01/BP_WeaponQualitySet_Pistol_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Pistol_01/BP_Projectile_Pistol_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Pistol_01/BP_Item_Pistol_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | Pistol_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/DA_Upgrade_Pistol_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Sprint Shooting

| Identity | Value |
| --- | --- |
| Id | Pistol_01_SprintShooting |
| Level | 5 |
| Level label | Amplified |
| Variant | Sprint Shooting |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 10 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 10 |
| Firearm critical/headshot multiplier | 2.5 |
| ARC armour multiplier | 0.2 |
| ARC armour propagation coefficient | 0.1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 500 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 12 |
| Reload time stat, seconds | 1.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.000536 |
| Base partial-reload duration, seconds | 1.4 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 10 | 10 |
| Armor | 0.6 | 0.4 | 0.2 | 1 | 0.08 | 0.8 | 0.8 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 4 | 4 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 15 | 15 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 15 | 15 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 12 | 12 |

##### Upgrades

###### Sprint Shooting

| Field | Value |
| --- | --- |
| Id | Pistol_01_SprintShooting |
| Name | Sprint Shooting |
| Description | Ergonomic fittings that allow the weapon to be comfortably fired while sprinting. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/DA_Upgrade_Pistol_01_SprintShooting.json |
| Modifier source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_01_SprintShooting.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_01_SprintShooting.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Blocksprintoverride**

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Bblocksprintduringprimaryuse | No |

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

None.

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 10 |
| Fire rate | 33.333 |
| Range | 35.532 |
| Stability | 71.689 |
| Agility | 89.391 |
| Stealth | 24 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Pistol_01/Curve_DamageFalloff_Pistol_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 13,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | -1 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Blocksprintoverride

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Bblocksprintduringprimaryuse | No |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/BP_Item_Pistol_01_SprintShooting.json |
| Item | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/DA_Item_Pistol_01_SprintShooting.json |
| Quality set | Content/Pioneer/Items/Firearms/Pistol_01/BP_WeaponQualitySet_Pistol_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Pistol_01/BP_WeaponQualitySet_Pistol_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Pistol_01/BP_Projectile_Pistol_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Pistol_01/BP_Item_Pistol_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | Pistol_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/DA_Upgrade_Pistol_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

<details>
<summary>Actual game source files</summary>

- [Content/Pioneer/Items/Firearms/Pistol_01/Ascended/BP_Item_Pistol_01_Ascended.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/Ascended/BP_Item_Pistol_01_Ascended.json)
- [Content/Pioneer/Items/Firearms/Pistol_01/Ascended/DA_Item_Pistol_01_Ascended.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/Ascended/DA_Item_Pistol_01_Ascended.json)
- [Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/BP_Item_Pistol_01_Burst.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/BP_Item_Pistol_01_Burst.json)
- [Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/BP_Item_Pistol_01_Burst_IncreasedBurst.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/BP_Item_Pistol_01_Burst_IncreasedBurst.json)
- [Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/BP_Item_Pistol_01_Burst_IncreasedBurst_SprintShooting.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/BP_Item_Pistol_01_Burst_IncreasedBurst_SprintShooting.json)
- [Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/BP_Item_Pistol_01_Burst_SprintShooting.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/BP_Item_Pistol_01_Burst_SprintShooting.json)
- [Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/BP_Item_Pistol_01_FullAuto.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/BP_Item_Pistol_01_FullAuto.json)
- [Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/BP_Item_Pistol_01_FullAuto_SprintShooting.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/BP_Item_Pistol_01_FullAuto_SprintShooting.json)
- [Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/BP_Item_Pistol_01_SprintShooting.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/BP_Item_Pistol_01_SprintShooting.json)
- [Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/DA_Item_Pistol_01_Burst.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/DA_Item_Pistol_01_Burst.json)
- [Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/DA_Item_Pistol_01_Burst_IncreasedBurst.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/DA_Item_Pistol_01_Burst_IncreasedBurst.json)
- [Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/DA_Item_Pistol_01_Burst_IncreasedBurst_SprintShooting.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/DA_Item_Pistol_01_Burst_IncreasedBurst_SprintShooting.json)
- [Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/DA_Item_Pistol_01_Burst_SprintShooting.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/DA_Item_Pistol_01_Burst_SprintShooting.json)
- [Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/DA_Item_Pistol_01_FullAuto.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/DA_Item_Pistol_01_FullAuto.json)
- [Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/DA_Item_Pistol_01_FullAuto_SprintShooting.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/DA_Item_Pistol_01_FullAuto_SprintShooting.json)
- [Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/DA_Item_Pistol_01_SprintShooting.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/DA_Item_Pistol_01_SprintShooting.json)
- [Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_01_Burst.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_01_Burst.json)
- [Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_01_FullAuto.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_01_FullAuto.json)
- [Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_01_IncreasedBurst.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_01_IncreasedBurst.json)
- [Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_01_SprintShooting.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_01_SprintShooting.json)
- [Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/DA_Upgrade_Pistol_01_Ascended.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/DA_Upgrade_Pistol_01_Ascended.json)
- [Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/DA_Upgrade_Pistol_01_Burst.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/DA_Upgrade_Pistol_01_Burst.json)
- [Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/DA_Upgrade_Pistol_01_FullAuto.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/DA_Upgrade_Pistol_01_FullAuto.json)
- [Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/DA_Upgrade_Pistol_01_IncreasedBurst.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/DA_Upgrade_Pistol_01_IncreasedBurst.json)
- [Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/DA_Upgrade_Pistol_01_SprintShooting.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/DA_Upgrade_Pistol_01_SprintShooting.json)
- [Content/Pioneer/Items/Firearms/Pistol_01/BP_Item_Pistol_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/BP_Item_Pistol_01.json)
- [Content/Pioneer/Items/Firearms/Pistol_01/BP_Projectile_Pistol_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/BP_Projectile_Pistol_01.json)
- [Content/Pioneer/Items/Firearms/Pistol_01/BP_WeaponQualitySet_Pistol_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/BP_WeaponQualitySet_Pistol_01.json)
- [Content/Pioneer/Items/Firearms/Pistol_01/Curve_DamageFalloff_Pistol_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/Curve_DamageFalloff_Pistol_01.json)
- [Content/Pioneer/Items/Firearms/Pistol_01/DA_Item_Pistol_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/DA_Item_Pistol_01.json)

</details>
