[Weapon index](README.md) · [Definitions and mechanics](Mechanics.md) · [JSON data](weapons.json)

# Bettina

Internal weapon id: `AssaultRifle_Heavy_01`. Ammo: **HeavyAmmo**.

### Standard levels

| Level / variant | Damage / projectile | Projectiles | Full spread | Crit × | ARC armour × | ARC weakpoint × | RPM | Magazine | Reload stat, s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I | 16 | 1 | 16 | 2 | 2 | 1 | 270 | 22 | 4.5 |
| II | 16 | 1 | 16 | 2 | 2 | 1 | 285 | 22 | 4 |
| III | 16 | 1 | 16 | 2 | 2 | 1 | 300 | 22 | 3.5 |
| IV | 16 | 1 | 16 | 2 | 2 | 1 | 315 | 22 | 3 |

#### Level I

| Identity | Value |
| --- | --- |
| Id | AssaultRifle_Heavy_01_Level1 |
| Level | 1 |
| Level label | I |
| Variant | Standard |
| Quality index | 0 |
| Uses standard level | 1 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 16 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 16 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 2 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 270 |
| Firing mode | Auto |
| Burst size stat | 1 |
| Magazine size | 22 |
| Reload time stat, seconds | 4.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.001317 |
| Base partial-reload duration, seconds | 3.2 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 16 | 16 |
| Armor | 0.6 | 0.4 | 2 | 1 | 0.8 | 12.8 | 12.8 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 6.4 | 6.4 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 24 | 24 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 24 | 24 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 19.2 | 19.2 |

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
| Damage | 16 |
| Fire rate | 17.5 |
| Range | 51.595 |
| Stability | 74.786 |
| Agility | 49.381 |
| Stealth | 14 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Curve_DamageFalloff_AssaultRifle_Heavy_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.0001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 18,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 20,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | 0.5 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Firerate

| Field | Value |
| --- | --- |
| Add | -15 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_Item_AssaultRifle_Heavy_01.json |
| Item | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/DA_Item_AssaultRifle_Heavy_01.json |
| Quality set | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_WeaponQualitySet_AssaultRifle_Heavy_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_WeaponQualitySet_AssaultRifle_Heavy_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_Projectile_AssaultRifle_Heavy_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_Item_AssaultRifle_Heavy_01.json, Script/PrecompiledScript.Cache

#### Level II

| Identity | Value |
| --- | --- |
| Id | AssaultRifle_Heavy_01_Level2 |
| Level | 2 |
| Level label | II |
| Variant | Standard |
| Quality index | 1 |
| Uses standard level | 2 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 16 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 16 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 2 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 285 |
| Firing mode | Auto |
| Burst size stat | 1 |
| Magazine size | 22 |
| Reload time stat, seconds | 4 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.001185 |
| Base partial-reload duration, seconds | 3.2 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 16 | 16 |
| Armor | 0.6 | 0.4 | 2 | 1 | 0.8 | 12.8 | 12.8 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 6.4 | 6.4 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 24 | 24 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 24 | 24 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 19.2 | 19.2 |

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
| Damage | 16 |
| Fire rate | 19 |
| Range | 51.595 |
| Stability | 72.786 |
| Agility | 49.381 |
| Stealth | 14 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Curve_DamageFalloff_AssaultRifle_Heavy_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.0001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 18,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 20,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

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
| Weapon | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_Item_AssaultRifle_Heavy_01.json |
| Item | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/DA_Item_AssaultRifle_Heavy_01.json |
| Quality set | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_WeaponQualitySet_AssaultRifle_Heavy_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_WeaponQualitySet_AssaultRifle_Heavy_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_Projectile_AssaultRifle_Heavy_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_Item_AssaultRifle_Heavy_01.json, Script/PrecompiledScript.Cache

#### Level III

| Identity | Value |
| --- | --- |
| Id | AssaultRifle_Heavy_01_Level3 |
| Level | 3 |
| Level label | III |
| Variant | Standard |
| Quality index | 2 |
| Uses standard level | 3 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 16 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 16 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 2 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 300 |
| Firing mode | Auto |
| Burst size stat | 1 |
| Magazine size | 22 |
| Reload time stat, seconds | 3.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.001054 |
| Base partial-reload duration, seconds | 3.2 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 16 | 16 |
| Armor | 0.6 | 0.4 | 2 | 1 | 0.8 | 12.8 | 12.8 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 6.4 | 6.4 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 24 | 24 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 24 | 24 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 19.2 | 19.2 |

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
| Damage | 16 |
| Fire rate | 20.5 |
| Range | 51.595 |
| Stability | 70.786 |
| Agility | 49.381 |
| Stealth | 14 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Curve_DamageFalloff_AssaultRifle_Heavy_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.0001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 18,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 20,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

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

###### Firerate

| Field | Value |
| --- | --- |
| Add | 15 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_Item_AssaultRifle_Heavy_01.json |
| Item | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/DA_Item_AssaultRifle_Heavy_01.json |
| Quality set | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_WeaponQualitySet_AssaultRifle_Heavy_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_WeaponQualitySet_AssaultRifle_Heavy_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_Projectile_AssaultRifle_Heavy_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_Item_AssaultRifle_Heavy_01.json, Script/PrecompiledScript.Cache

#### Level IV

| Identity | Value |
| --- | --- |
| Id | AssaultRifle_Heavy_01_Level4 |
| Level | 4 |
| Level label | IV |
| Variant | Standard |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 16 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 16 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 2 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 315 |
| Firing mode | Auto |
| Burst size stat | 1 |
| Magazine size | 22 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.000922 |
| Base partial-reload duration, seconds | 3.2 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 16 | 16 |
| Armor | 0.6 | 0.4 | 2 | 1 | 0.8 | 12.8 | 12.8 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 6.4 | 6.4 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 24 | 24 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 24 | 24 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 19.2 | 19.2 |

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
| Damage | 16 |
| Fire rate | 22 |
| Range | 51.595 |
| Stability | 68.786 |
| Agility | 49.381 |
| Stealth | 14 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Curve_DamageFalloff_AssaultRifle_Heavy_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.0001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 18,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 20,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

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

###### Firerate

| Field | Value |
| --- | --- |
| Add | 30 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_Item_AssaultRifle_Heavy_01.json |
| Item | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/DA_Item_AssaultRifle_Heavy_01.json |
| Quality set | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_WeaponQualitySet_AssaultRifle_Heavy_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_WeaponQualitySet_AssaultRifle_Heavy_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_Projectile_AssaultRifle_Heavy_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_Item_AssaultRifle_Heavy_01.json, Script/PrecompiledScript.Cache

### Amplified configurations

| Level / variant | Damage / projectile | Projectiles | Full spread | Crit × | ARC armour × | ARC weakpoint × | RPM | Magazine | Reload stat, s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Default | 16 | 1 | 16 | 2 | 2 | 1 | 315 | 22 | 3 |
| Bigger Mag | 16 | 1 | 16 | 2 | 2 | 1 | 315 | 37 | 3 |
| Semi-Auto | 19 | 1 | 19 | 2 | 2 | 1 | — | 22 | 3 |
| Semi-Auto + X-Rounds | 22 | 1 | 22 | 2 | 2.5 | 1 | — | 18 | 3 |

#### Amplified — Default

| Identity | Value |
| --- | --- |
| Id | AssaultRifle_Heavy_01_Ascended |
| Level | 5 |
| Level label | Amplified |
| Variant | Default |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 16 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 16 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 2 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 315 |
| Firing mode | Auto |
| Burst size stat | 1 |
| Magazine size | 22 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.000461 |
| Base partial-reload duration, seconds | 3.2 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 16 | 16 |
| Armor | 0.6 | 0.4 | 2 | 1 | 0.8 | 12.8 | 12.8 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 6.4 | 6.4 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 24 | 24 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 24 | 24 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 19.2 | 19.2 |

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
| Damage | 16 |
| Fire rate | 22 |
| Range | 51.595 |
| Stability | 68.786 |
| Agility | 49.381 |
| Stealth | 14 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Curve_DamageFalloff_AssaultRifle_Heavy_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.0001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 18,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 20,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

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

###### Firerate

| Field | Value |
| --- | --- |
| Add | 30 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/BP_Item_AssaultRifle_Heavy_01_Ascended.json |
| Item | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/DA_Item_AssaultRifle_Heavy_01_Ascended.json |
| Quality set | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_WeaponQualitySet_AssaultRifle_Heavy_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_WeaponQualitySet_AssaultRifle_Heavy_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_Projectile_AssaultRifle_Heavy_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_Item_AssaultRifle_Heavy_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | AssaultRifle_Heavy_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_Heavy_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Bigger Mag

| Identity | Value |
| --- | --- |
| Id | AssaultRifle_Heavy_01_BiggerMag |
| Level | 5 |
| Level label | Amplified |
| Variant | Bigger Mag |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 16 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 16 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 2 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 315 |
| Firing mode | Auto |
| Burst size stat | 1 |
| Magazine size | 37 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.000461 |
| Base partial-reload duration, seconds | 3.2 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 16 | 16 |
| Armor | 0.6 | 0.4 | 2 | 1 | 0.8 | 12.8 | 12.8 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 6.4 | 6.4 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 24 | 24 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 24 | 24 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 19.2 | 19.2 |

##### Upgrades

###### Bigger Mag

| Field | Value |
| --- | --- |
| Id | AssaultRifle_Heavy_01_BiggerMag |
| Name | Bigger Mag |
| Description | Increases the magazine capacity. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_Heavy_01_BiggerMag.json |
| Modifier source path | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_Heavy_01_BiggerMag.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_Heavy_01_BiggerMag.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Clipsize**

| Field | Value |
| --- | --- |
| Add | 15 |
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
| Damage | 16 |
| Fire rate | 22 |
| Range | 51.595 |
| Stability | 68.786 |
| Agility | 49.381 |
| Stealth | 14 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Curve_DamageFalloff_AssaultRifle_Heavy_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.0001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 18,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 20,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

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

###### Firerate

| Field | Value |
| --- | --- |
| Add | 30 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 15 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Permutations/BP_Item_AssaultRifle_Heavy_01_BiggerMag.json |
| Item | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Permutations/DA_Item_AssaultRifle_Heavy_01_BiggerMag.json |
| Quality set | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_WeaponQualitySet_AssaultRifle_Heavy_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_WeaponQualitySet_AssaultRifle_Heavy_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_Projectile_AssaultRifle_Heavy_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_Item_AssaultRifle_Heavy_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | AssaultRifle_Heavy_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_Heavy_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Semi-Auto

| Identity | Value |
| --- | --- |
| Id | AssaultRifle_Heavy_01_SemiAuto |
| Level | 5 |
| Level label | Amplified |
| Variant | Semi-Auto |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 19 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 19 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 2 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | — |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 22 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.000461 |
| Base partial-reload duration, seconds | 3.2 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 19 | 19 |
| Armor | 0.6 | 0.4 | 2 | 1 | 0.8 | 15.2 | 15.2 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 7.6 | 7.6 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 28.5 | 28.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 28.5 | 28.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 22.8 | 22.8 |

##### Upgrades

###### Semi-Auto

| Field | Value |
| --- | --- |
| Id | AssaultRifle_Heavy_01_SemiAuto |
| Name | Semi-Auto |
| Description | Makes the weapon semi-automatic. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_Heavy_01_SemiAuto.json |
| Modifier source path | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_Heavy_01_SingleFire.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_Heavy_01_SingleFire.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Firingmodeoverride**

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Currentfiringmode | EFiringMode::SemiAuto |

**Physicaldamage**

| Field | Value |
| --- | --- |
| Add | 3 |
| Addmultiply | 1 |
| Multiply | 1 |

**Firedispersiongain**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.8 |
| Multiply | 1 |

**Firedispersionmax**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.8 |
| Multiply | 1 |

**Dispersionrecoveryspeed**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 2 |
| Multiply | 1 |

**Recoilrecoverytime**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.2 |
| Multiply | 1 |

**Firerate**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.8 |
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
| Damage | 19 |
| Fire rate | 19.8 |
| Range | 55.339 |
| Stability | 74.414 |
| Agility | 49.381 |
| Stealth | 14 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Curve_DamageFalloff_AssaultRifle_Heavy_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.0001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 18,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 20,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Unresolved stats

###### Firerate

| Field | Value |
| --- | --- |
| Reason | Add and AddMultiply are both active; native CalculateCurrent operation order was not recovered. |
| Base | 285 |

**Modifier**

| Field | Value |
| --- | --- |
| Add | 30 |
| Addmultiply | 0.8 |
| Multiply | 1 |

**Candidate values**

252, 258

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

###### Firerate

| Field | Value |
| --- | --- |
| Add | 30 |
| Addmultiply | 0.8 |
| Multiply | 1 |

###### Firingmodeoverride

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Currentfiringmode | EFiringMode::SemiAuto |

###### Physicaldamage

| Field | Value |
| --- | --- |
| Add | 3 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Firedispersiongain

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.8 |
| Multiply | 1 |

###### Firedispersionmax

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.8 |
| Multiply | 1 |

###### Dispersionrecoveryspeed

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 2 |
| Multiply | 1 |

###### Recoilrecoverytime

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.2 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Permutations/BP_Item_AssaultRifle_Heavy_01_SemiAuto.json |
| Item | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Permutations/DA_Item_AssaultRifle_Heavy_01_SemiAuto.json |
| Quality set | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_WeaponQualitySet_AssaultRifle_Heavy_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_WeaponQualitySet_AssaultRifle_Heavy_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_Projectile_AssaultRifle_Heavy_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_Item_AssaultRifle_Heavy_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | AssaultRifle_Heavy_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_Heavy_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Semi-Auto + X-Rounds

| Identity | Value |
| --- | --- |
| Id | AssaultRifle_Heavy_01_SemiAuto_XRounds |
| Level | 5 |
| Level label | Amplified |
| Variant | Semi-Auto + X-Rounds |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 22 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 22 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 2.5 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | — |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 18 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.000461 |
| Base partial-reload duration, seconds | 3.2 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 22 | 22 |
| Armor | 0.6 | 0.4 | 2.5 | 1 | 1 | 22 | 22 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 8.8 | 8.8 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 33 | 33 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 33 | 33 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 26.4 | 26.4 |

##### Upgrades

###### Semi-Auto

| Field | Value |
| --- | --- |
| Id | AssaultRifle_Heavy_01_SemiAuto |
| Name | Semi-Auto |
| Description | Makes the weapon semi-automatic. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_Heavy_01_SemiAuto.json |
| Modifier source path | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_Heavy_01_SingleFire.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_Heavy_01_SingleFire.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Firingmodeoverride**

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Currentfiringmode | EFiringMode::SemiAuto |

**Physicaldamage**

| Field | Value |
| --- | --- |
| Add | 3 |
| Addmultiply | 1 |
| Multiply | 1 |

**Firedispersiongain**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.8 |
| Multiply | 1 |

**Firedispersionmax**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.8 |
| Multiply | 1 |

**Dispersionrecoveryspeed**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 2 |
| Multiply | 1 |

**Recoilrecoverytime**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.2 |
| Multiply | 1 |

**Firerate**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.8 |
| Multiply | 1 |

###### X-Rounds

| Field | Value |
| --- | --- |
| Id | AssaultRifle_Heavy_01_XRounds |
| Name | X-Rounds |
| Description | Adds an explosive compound to the projectile, dealing slightly increased damage to Raiders and significantly increased damage to ARC Armor plating. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_Heavy_01_XRounds.json |
| Modifier source path | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_Heavy_01_XRounds.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_Heavy_01_XRounds.uasset |
| Modifier selection | baked_cache_enabled |

**Modifiers**

**Physicaldamage**

| Field | Value |
| --- | --- |
| Add | 3 |
| Addmultiply | 1 |
| Multiply | 1 |

**Clipsize**

| Field | Value |
| --- | --- |
| Add | -4 |
| Addmultiply | 1 |
| Multiply | 1 |

**Horizontalrecoil**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.2 |
| Multiply | 1 |

**Verticalrecoil**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.2 |
| Multiply | 1 |

**Launchspeed**

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
| Damage | 22 |
| Fire rate | 19.8 |
| Range | 47.339 |
| Stability | 68.55501 |
| Agility | 49.381 |
| Stealth | 10 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Curve_DamageFalloff_AssaultRifle_Heavy_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.0001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 18,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 20,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Unresolved stats

###### Firerate

| Field | Value |
| --- | --- |
| Reason | Add and AddMultiply are both active; native CalculateCurrent operation order was not recovered. |
| Base | 285 |

**Modifier**

| Field | Value |
| --- | --- |
| Add | 30 |
| Addmultiply | 0.8 |
| Multiply | 1 |

**Candidate values**

252, 258

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

###### Firerate

| Field | Value |
| --- | --- |
| Add | 30 |
| Addmultiply | 0.8 |
| Multiply | 1 |

###### Firingmodeoverride

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Currentfiringmode | EFiringMode::SemiAuto |

###### Physicaldamage

| Field | Value |
| --- | --- |
| Add | 6 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Firedispersiongain

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.8 |
| Multiply | 1 |

###### Firedispersionmax

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.8 |
| Multiply | 1 |

###### Dispersionrecoveryspeed

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 2 |
| Multiply | 1 |

###### Recoilrecoverytime

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.2 |
| Multiply | 1 |

###### Clipsize

| Field | Value |
| --- | --- |
| Add | -4 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Horizontalrecoil

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.2 |
| Multiply | 1 |

###### Verticalrecoil

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.2 |
| Multiply | 1 |

###### Launchspeed

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.6 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Permutations/BP_Item_AssaultRifle_Heavy_01_SemiAuto_XRounds.json |
| Item | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Permutations/DA_Item_AssaultRifle_Heavy_01_SemiAuto_XRounds.json |
| Quality set | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_WeaponQualitySet_AssaultRifle_Heavy_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_WeaponQualitySet_AssaultRifle_Heavy_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/BP_Projectile_AssaultRifle_Heavy_01_XRounds.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Permutations/BP_Item_AssaultRifle_Heavy_01_SemiAuto_XRounds.json, Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_Item_AssaultRifle_Heavy_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | AssaultRifle_Heavy_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_Heavy_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

<details>
<summary>Actual game source files</summary>

- [Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/BP_Item_AssaultRifle_Heavy_01_Ascended.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/BP_Item_AssaultRifle_Heavy_01_Ascended.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/BP_Projectile_AssaultRifle_Heavy_01_XRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/BP_Projectile_AssaultRifle_Heavy_01_XRounds.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/DA_Item_AssaultRifle_Heavy_01_Ascended.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/DA_Item_AssaultRifle_Heavy_01_Ascended.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Permutations/BP_Item_AssaultRifle_Heavy_01_BiggerMag.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Permutations/BP_Item_AssaultRifle_Heavy_01_BiggerMag.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Permutations/BP_Item_AssaultRifle_Heavy_01_SemiAuto.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Permutations/BP_Item_AssaultRifle_Heavy_01_SemiAuto.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Permutations/BP_Item_AssaultRifle_Heavy_01_SemiAuto_XRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Permutations/BP_Item_AssaultRifle_Heavy_01_SemiAuto_XRounds.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Permutations/DA_Item_AssaultRifle_Heavy_01_BiggerMag.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Permutations/DA_Item_AssaultRifle_Heavy_01_BiggerMag.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Permutations/DA_Item_AssaultRifle_Heavy_01_SemiAuto.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Permutations/DA_Item_AssaultRifle_Heavy_01_SemiAuto.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Permutations/DA_Item_AssaultRifle_Heavy_01_SemiAuto_XRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Permutations/DA_Item_AssaultRifle_Heavy_01_SemiAuto_XRounds.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_Heavy_01_BiggerMag.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_Heavy_01_BiggerMag.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_Heavy_01_SingleFire.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_Heavy_01_SingleFire.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_Heavy_01_XRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_Heavy_01_XRounds.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_Heavy_01_Ascended.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_Heavy_01_Ascended.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_Heavy_01_BiggerMag.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_Heavy_01_BiggerMag.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_Heavy_01_SemiAuto.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_Heavy_01_SemiAuto.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_Heavy_01_XRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_Heavy_01_XRounds.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_Item_AssaultRifle_Heavy_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_Item_AssaultRifle_Heavy_01.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_Projectile_AssaultRifle_Heavy_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_Projectile_AssaultRifle_Heavy_01.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_WeaponQualitySet_AssaultRifle_Heavy_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/BP_WeaponQualitySet_AssaultRifle_Heavy_01.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Curve_DamageFalloff_AssaultRifle_Heavy_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/Curve_DamageFalloff_AssaultRifle_Heavy_01.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/DA_Item_AssaultRifle_Heavy_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Heavy_01/DA_Item_AssaultRifle_Heavy_01.json)

</details>
