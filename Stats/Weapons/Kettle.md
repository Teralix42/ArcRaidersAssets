[Weapon index](README.md) · [Definitions and mechanics](Mechanics.md) · [JSON data](weapons.json)

# Kettle

Internal weapon id: `AssaultRifle_Pneumatic_01`. Ammo: **LightAmmo**.

### Standard levels

| Level / variant | Damage / projectile | Projectiles | Full spread | Crit × | ARC armour × | ARC weakpoint × | RPM | Magazine | Reload stat, s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I | 8.5 | 1 | 8.5 | 2.5 | 0.2 | 1 | 450 | 20 | 5 |
| II | 8.5 | 1 | 8.5 | 2.5 | 0.2 | 1 | 450 | 20 | 4.5 |
| III | 8.5 | 1 | 8.5 | 2.5 | 0.2 | 1 | 450 | 20 | 4 |
| IV | 8.5 | 1 | 8.5 | 2.5 | 0.2 | 1 | 450 | 20 | 3.5 |

#### Level I

| Identity | Value |
| --- | --- |
| Id | AssaultRifle_Pneumatic_01_Level1 |
| Level | 1 |
| Level label | I |
| Variant | Standard |
| Quality index | 0 |
| Uses standard level | 1 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 8.5 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 8.5 |
| Firearm critical/headshot multiplier | 2.5 |
| ARC armour multiplier | 0.2 |
| ARC armour propagation coefficient | 0.1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 450 |
| Firing mode | Single |
| Burst size stat | 1 |
| Magazine size | 20 |
| Reload time stat, seconds | 5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.001607 |
| Base partial-reload duration, seconds | 4.5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 8.5 | 8.5 |
| Armor | 0.6 | 0.4 | 0.2 | 1 | 0.08 | 0.68 | 0.68 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.4 | 3.4 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 12.75 | 12.75 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 12.75 | 12.75 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 10.2 | 10.2 |

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
| Damage | 8.5 |
| Fire rate | 30 |
| Range | 37.904 |
| Stability | 73.256 |
| Agility | 58.514 |
| Stealth | 26 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Curve_DamageFalloff_AssaultRifle_Pneumatic_01.json |

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

###### Launchspeed

| Field | Value |
| --- | --- |
| Add | -8,000 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_Item_AssaultRifle_Pneumatic_01.json |
| Item | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/DA_Item_AssaultRifle_Pneumatic_01.json |
| Quality set | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_WeaponQualitySet_AssaultRifle_Pneumatic_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_WeaponQualitySet_AssaultRifle_Pneumatic_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_Projectile_AssaultRifle_Pneumatic_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_Item_AssaultRifle_Pneumatic_01.json, Script/PrecompiledScript.Cache

#### Level II

| Identity | Value |
| --- | --- |
| Id | AssaultRifle_Pneumatic_01_Level2 |
| Level | 2 |
| Level label | II |
| Variant | Standard |
| Quality index | 1 |
| Uses standard level | 2 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 8.5 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 8.5 |
| Firearm critical/headshot multiplier | 2.5 |
| ARC armour multiplier | 0.2 |
| ARC armour propagation coefficient | 0.1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 450 |
| Firing mode | Single |
| Burst size stat | 1 |
| Magazine size | 20 |
| Reload time stat, seconds | 4.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.001446 |
| Base partial-reload duration, seconds | 4.5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 8.5 | 8.5 |
| Armor | 0.6 | 0.4 | 0.2 | 1 | 0.08 | 0.68 | 0.68 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.4 | 3.4 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 12.75 | 12.75 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 12.75 | 12.75 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 10.2 | 10.2 |

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
| Damage | 8.5 |
| Fire rate | 30 |
| Range | 42.904 |
| Stability | 73.256 |
| Agility | 58.514 |
| Stealth | 26 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Curve_DamageFalloff_AssaultRifle_Pneumatic_01.json |

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
| Weapon | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_Item_AssaultRifle_Pneumatic_01.json |
| Item | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/DA_Item_AssaultRifle_Pneumatic_01.json |
| Quality set | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_WeaponQualitySet_AssaultRifle_Pneumatic_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_WeaponQualitySet_AssaultRifle_Pneumatic_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_Projectile_AssaultRifle_Pneumatic_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_Item_AssaultRifle_Pneumatic_01.json, Script/PrecompiledScript.Cache

#### Level III

| Identity | Value |
| --- | --- |
| Id | AssaultRifle_Pneumatic_01_Level3 |
| Level | 3 |
| Level label | III |
| Variant | Standard |
| Quality index | 2 |
| Uses standard level | 3 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 8.5 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 8.5 |
| Firearm critical/headshot multiplier | 2.5 |
| ARC armour multiplier | 0.2 |
| ARC armour propagation coefficient | 0.1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 450 |
| Firing mode | Single |
| Burst size stat | 1 |
| Magazine size | 20 |
| Reload time stat, seconds | 4 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.001286 |
| Base partial-reload duration, seconds | 4.5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 8.5 | 8.5 |
| Armor | 0.6 | 0.4 | 0.2 | 1 | 0.08 | 0.68 | 0.68 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.4 | 3.4 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 12.75 | 12.75 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 12.75 | 12.75 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 10.2 | 10.2 |

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
| Damage | 8.5 |
| Fire rate | 30 |
| Range | 47.904 |
| Stability | 73.256 |
| Agility | 58.514 |
| Stealth | 26 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Curve_DamageFalloff_AssaultRifle_Pneumatic_01.json |

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

###### Launchspeed

| Field | Value |
| --- | --- |
| Add | 8,000 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_Item_AssaultRifle_Pneumatic_01.json |
| Item | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/DA_Item_AssaultRifle_Pneumatic_01.json |
| Quality set | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_WeaponQualitySet_AssaultRifle_Pneumatic_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_WeaponQualitySet_AssaultRifle_Pneumatic_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_Projectile_AssaultRifle_Pneumatic_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_Item_AssaultRifle_Pneumatic_01.json, Script/PrecompiledScript.Cache

#### Level IV

| Identity | Value |
| --- | --- |
| Id | AssaultRifle_Pneumatic_01_Level4 |
| Level | 4 |
| Level label | IV |
| Variant | Standard |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 8.5 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 8.5 |
| Firearm critical/headshot multiplier | 2.5 |
| ARC armour multiplier | 0.2 |
| ARC armour propagation coefficient | 0.1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 450 |
| Firing mode | Single |
| Burst size stat | 1 |
| Magazine size | 20 |
| Reload time stat, seconds | 3.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.001125 |
| Base partial-reload duration, seconds | 4.5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 8.5 | 8.5 |
| Armor | 0.6 | 0.4 | 0.2 | 1 | 0.08 | 0.68 | 0.68 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.4 | 3.4 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 12.75 | 12.75 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 12.75 | 12.75 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 10.2 | 10.2 |

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
| Damage | 8.5 |
| Fire rate | 30 |
| Range | 52.404 |
| Stability | 73.256 |
| Agility | 58.514 |
| Stealth | 26 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Curve_DamageFalloff_AssaultRifle_Pneumatic_01.json |

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

###### Launchspeed

| Field | Value |
| --- | --- |
| Add | 16,000 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_Item_AssaultRifle_Pneumatic_01.json |
| Item | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/DA_Item_AssaultRifle_Pneumatic_01.json |
| Quality set | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_WeaponQualitySet_AssaultRifle_Pneumatic_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_WeaponQualitySet_AssaultRifle_Pneumatic_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_Projectile_AssaultRifle_Pneumatic_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_Item_AssaultRifle_Pneumatic_01.json, Script/PrecompiledScript.Cache

### Amplified configurations

| Level / variant | Damage / projectile | Projectiles | Full spread | Crit × | ARC armour × | ARC weakpoint × | RPM | Magazine | Reload stat, s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Default | 8.5 | 1 | 8.5 | 2.5 | 0.2 | 1 | 450 | 20 | 3.5 |
| Anti-Shield | 6.5 | 1 | 6.5 | 2.5 | 0.2 | 1 | 450 | 20 | 3.5 |
| Anti-Shield + Full-Auto | 6.5 | 1 | 6.5 | 2 | 0.2 | 1 | 517.5 | 20 | 3.5 |
| Full-Auto | 8.5 | 1 | 8.5 | 2 | 0.2 | 1 | 517.5 | 20 | 3.5 |
| X-Rounds | 15 | 1 | 15 | 2.5 | 1 | 1 | 360 | 16 | 3.5 |

#### Amplified — Default

| Identity | Value |
| --- | --- |
| Id | AssaultRifle_Pneumatic_01_Ascended |
| Level | 5 |
| Level label | Amplified |
| Variant | Default |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 8.5 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 8.5 |
| Firearm critical/headshot multiplier | 2.5 |
| ARC armour multiplier | 0.2 |
| ARC armour propagation coefficient | 0.1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 450 |
| Firing mode | Single |
| Burst size stat | 1 |
| Magazine size | 20 |
| Reload time stat, seconds | 3.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.000562 |
| Base partial-reload duration, seconds | 4.5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 8.5 | 8.5 |
| Armor | 0.6 | 0.4 | 0.2 | 1 | 0.08 | 0.68 | 0.68 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.4 | 3.4 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 12.75 | 12.75 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 12.75 | 12.75 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 10.2 | 10.2 |

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
| Damage | 8.5 |
| Fire rate | 30 |
| Range | 52.404 |
| Stability | 73.256 |
| Agility | 58.514 |
| Stealth | 26 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Curve_DamageFalloff_AssaultRifle_Pneumatic_01.json |

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

###### Launchspeed

| Field | Value |
| --- | --- |
| Add | 16,000 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/BP_Item_AssaultRifle_Pneumatic_01_Ascended.json |
| Item | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/DA_Item_AssaultRifle_Pneumatic_01_Ascended.json |
| Quality set | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_WeaponQualitySet_AssaultRifle_Pneumatic_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_WeaponQualitySet_AssaultRifle_Pneumatic_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_Projectile_AssaultRifle_Pneumatic_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_Item_AssaultRifle_Pneumatic_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | AssaultRifle_Pneumatic_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_Pneumatic_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Anti-Shield

| Identity | Value |
| --- | --- |
| Id | AssaultRifle_Pneumatic_01_AntiShield |
| Level | 5 |
| Level label | Amplified |
| Variant | Anti-Shield |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 6.5 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 6.5 |
| Firearm critical/headshot multiplier | 2.5 |
| ARC armour multiplier | 0.2 |
| ARC armour propagation coefficient | 0.1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 450 |
| Firing mode | Single |
| Burst size stat | 1 |
| Magazine size | 20 |
| Reload time stat, seconds | 3.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.000562 |
| Base partial-reload duration, seconds | 4.5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 6.5 | 6.5 |
| Armor | 0.6 | 0.4 | 0.2 | 1 | 0.08 | 0.52 | 0.52 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 2.6 | 2.6 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 9.75 | 9.75 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 9.75 | 9.75 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 7.8 | 7.8 |

##### Upgrades

###### Anti-Shield

| Field | Value |
| --- | --- |
| Id | AssaultRifle_Pneumatic_01_AntiShield |
| Name | Anti-Shield |
| Description | Redistributes damage to prioritize breaking shields faster. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_Pneumatic_01_AntiShield.json |
| Modifier source path | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_Pneumatic_01_AntiShield.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_Pneumatic_01_AntiShield.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Physicaldamage**

| Field | Value |
| --- | --- |
| Add | -2 |
| Addmultiply | 1 |
| Multiply | 1 |

**Playerarmordamagebonus**

| Field | Value |
| --- | --- |
| Add | 1.5 |
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
| Damage | 6.5 |
| Fire rate | 30 |
| Range | 52.404 |
| Stability | 73.256 |
| Agility | 58.514 |
| Stealth | 26 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Curve_DamageFalloff_AssaultRifle_Pneumatic_01.json |

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

###### Launchspeed

| Field | Value |
| --- | --- |
| Add | 16,000 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Physicaldamage

| Field | Value |
| --- | --- |
| Add | -2 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Playerarmordamagebonus

| Field | Value |
| --- | --- |
| Add | 1.5 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Permutations/BP_Item_AssaultRifle_Pneumatic_01_AntiShield.json |
| Item | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Permutations/DA_Item_AssaultRifle_Pneumatic_01_AntiShield.json |
| Quality set | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_WeaponQualitySet_AssaultRifle_Pneumatic_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_WeaponQualitySet_AssaultRifle_Pneumatic_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/BP_Projectile_AssaultRifle_Pneumatic_01_AntiShield.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_Item_AssaultRifle_Pneumatic_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | AssaultRifle_Pneumatic_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_Pneumatic_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Anti-Shield + Full-Auto

| Identity | Value |
| --- | --- |
| Id | AssaultRifle_Pneumatic_01_AntiShield_FullAuto |
| Level | 5 |
| Level label | Amplified |
| Variant | Anti-Shield + Full-Auto |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 6.5 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 6.5 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 0.2 |
| ARC armour propagation coefficient | 0.1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 517.5 |
| Firing mode | Auto |
| Burst size stat | 1 |
| Magazine size | 20 |
| Reload time stat, seconds | 3.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.000562 |
| Base partial-reload duration, seconds | 4.5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 6.5 | 6.5 |
| Armor | 0.6 | 0.4 | 0.2 | 1 | 0.08 | 0.52 | 0.52 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 2.6 | 2.6 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 9.75 | 9.75 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 9.75 | 9.75 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 7.8 | 7.8 |

##### Upgrades

###### Anti-Shield

| Field | Value |
| --- | --- |
| Id | AssaultRifle_Pneumatic_01_AntiShield |
| Name | Anti-Shield |
| Description | Redistributes damage to prioritize breaking shields faster. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_Pneumatic_01_AntiShield.json |
| Modifier source path | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_Pneumatic_01_AntiShield.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_Pneumatic_01_AntiShield.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Physicaldamage**

| Field | Value |
| --- | --- |
| Add | -2 |
| Addmultiply | 1 |
| Multiply | 1 |

**Playerarmordamagebonus**

| Field | Value |
| --- | --- |
| Add | 1.5 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Full-Auto

| Field | Value |
| --- | --- |
| Id | AssaultRifle_Pneumatic_01_FullAuto |
| Name | Full-Auto |
| Description | Makes the weapon fully automatic, at the cost of accuracy and stability. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_Pneumatic_01_FullAuto.json |
| Modifier source path | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_Pneumatic_01_FullAuto.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_Pneumatic_01_FullAuto.uasset |
| Modifier selection | baked_cache_enabled |

**Modifiers**

**Criticaldamagemultiplier**

| Field | Value |
| --- | --- |
| Add | -0.5 |
| Addmultiply | 1 |
| Multiply | 1 |

**Firerate**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.15 |
| Multiply | 1 |

**Horizontalrecoil**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.3 |
| Multiply | 1 |

**Verticalrecoil**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.3 |
| Multiply | 1 |

**Firedispersionmax**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.3 |
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
| Damage | 6.5 |
| Fire rate | 34.5 |
| Range | 52.404 |
| Stability | 65.147 |
| Agility | 58.514 |
| Stealth | 26 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Curve_DamageFalloff_AssaultRifle_Pneumatic_01.json |

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

###### Launchspeed

| Field | Value |
| --- | --- |
| Add | 16,000 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Physicaldamage

| Field | Value |
| --- | --- |
| Add | -2 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Playerarmordamagebonus

| Field | Value |
| --- | --- |
| Add | 1.5 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Criticaldamagemultiplier

| Field | Value |
| --- | --- |
| Add | -0.5 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Firerate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.15 |
| Multiply | 1 |

###### Horizontalrecoil

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.3 |
| Multiply | 1 |

###### Verticalrecoil

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.3 |
| Multiply | 1 |

###### Firedispersionmax

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.3 |
| Multiply | 1 |

###### Firingmodeoverride

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Currentfiringmode | EFiringMode::Auto |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Permutations/BP_Item_AssaultRifle_Pneumatic_01_AntiShield_FullAuto.json |
| Item | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Permutations/DA_Item_AssaultRifle_Pneumatic_01_AntiShield_FullAuto.json |
| Quality set | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_WeaponQualitySet_AssaultRifle_Pneumatic_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_WeaponQualitySet_AssaultRifle_Pneumatic_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/BP_Projectile_AssaultRifle_Pneumatic_01_AntiShield.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_Item_AssaultRifle_Pneumatic_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | AssaultRifle_Pneumatic_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_Pneumatic_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Full-Auto

| Identity | Value |
| --- | --- |
| Id | AssaultRifle_Pneumatic_01_FullAuto |
| Level | 5 |
| Level label | Amplified |
| Variant | Full-Auto |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 8.5 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 8.5 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 0.2 |
| ARC armour propagation coefficient | 0.1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 517.5 |
| Firing mode | Auto |
| Burst size stat | 1 |
| Magazine size | 20 |
| Reload time stat, seconds | 3.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.000562 |
| Base partial-reload duration, seconds | 4.5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 8.5 | 8.5 |
| Armor | 0.6 | 0.4 | 0.2 | 1 | 0.08 | 0.68 | 0.68 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.4 | 3.4 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 12.75 | 12.75 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 12.75 | 12.75 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 10.2 | 10.2 |

##### Upgrades

###### Full-Auto

| Field | Value |
| --- | --- |
| Id | AssaultRifle_Pneumatic_01_FullAuto |
| Name | Full-Auto |
| Description | Makes the weapon fully automatic, at the cost of accuracy and stability. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_Pneumatic_01_FullAuto.json |
| Modifier source path | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_Pneumatic_01_FullAuto.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_Pneumatic_01_FullAuto.uasset |
| Modifier selection | baked_cache_enabled |

**Modifiers**

**Criticaldamagemultiplier**

| Field | Value |
| --- | --- |
| Add | -0.5 |
| Addmultiply | 1 |
| Multiply | 1 |

**Firerate**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.15 |
| Multiply | 1 |

**Horizontalrecoil**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.3 |
| Multiply | 1 |

**Verticalrecoil**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.3 |
| Multiply | 1 |

**Firedispersionmax**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.3 |
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
| Damage | 8.5 |
| Fire rate | 34.5 |
| Range | 52.404 |
| Stability | 65.147 |
| Agility | 58.514 |
| Stealth | 26 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Curve_DamageFalloff_AssaultRifle_Pneumatic_01.json |

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

###### Launchspeed

| Field | Value |
| --- | --- |
| Add | 16,000 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Criticaldamagemultiplier

| Field | Value |
| --- | --- |
| Add | -0.5 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Firerate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.15 |
| Multiply | 1 |

###### Horizontalrecoil

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.3 |
| Multiply | 1 |

###### Verticalrecoil

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.3 |
| Multiply | 1 |

###### Firedispersionmax

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.3 |
| Multiply | 1 |

###### Firingmodeoverride

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Currentfiringmode | EFiringMode::Auto |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Permutations/BP_Item_AssaultRifle_Pneumatic_01_FullAuto.json |
| Item | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Permutations/DA_Item_AssaultRifle_Pneumatic_01_FullAuto.json |
| Quality set | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_WeaponQualitySet_AssaultRifle_Pneumatic_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_WeaponQualitySet_AssaultRifle_Pneumatic_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_Projectile_AssaultRifle_Pneumatic_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_Item_AssaultRifle_Pneumatic_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | AssaultRifle_Pneumatic_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_Pneumatic_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — X-Rounds

| Identity | Value |
| --- | --- |
| Id | AssaultRifle_Pneumatic_01_XRounds |
| Level | 5 |
| Level label | Amplified |
| Variant | X-Rounds |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 15 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 15 |
| Firearm critical/headshot multiplier | 2.5 |
| ARC armour multiplier | 1 |
| ARC armour propagation coefficient | 0.1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 360 |
| Firing mode | Single |
| Burst size stat | 1 |
| Magazine size | 16 |
| Reload time stat, seconds | 3.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.000562 |
| Base partial-reload duration, seconds | 4.5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 15 | 15 |
| Armor | 0.6 | 0.4 | 1 | 1 | 0.4 | 6 | 6 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 6 | 6 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 22.5 | 22.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 22.5 | 22.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 18 | 18 |

##### Upgrades

###### X-Rounds

| Field | Value |
| --- | --- |
| Id | AssaultRifle_Pneumatic_01_XRounds |
| Name | X-Rounds |
| Description | Adds an explosive compound to the projectile, dealing slightly increased damage to Raiders and significantly increased damage to ARC Armor plating. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_Pneumatic_01_XRounds.json |
| Modifier source path | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_Pneumatic_01_XRounds.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_Pneumatic_01_XRounds.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Physicaldamage**

| Field | Value |
| --- | --- |
| Add | 6.5 |
| Addmultiply | 1 |
| Multiply | 1 |

**Launchspeed**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

**Verticalrecoil**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.15 |
| Multiply | 1 |

**Horizontalrecoil**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.15 |
| Multiply | 1 |

**Clipsize**

| Field | Value |
| --- | --- |
| Add | -4 |
| Addmultiply | 1 |
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
| Damage | 15 |
| Fire rate | 24 |
| Range | 51.284 |
| Stability | 75.927 |
| Agility | 58.514 |
| Stealth | 20 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Curve_DamageFalloff_AssaultRifle_Pneumatic_01.json |

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

###### Launchspeed

| Field | Value |
| --- | --- |
| Add | 16,000 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Physicaldamage

| Field | Value |
| --- | --- |
| Add | 6.5 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Verticalrecoil

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.15 |
| Multiply | 1 |

###### Horizontalrecoil

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.15 |
| Multiply | 1 |

###### Clipsize

| Field | Value |
| --- | --- |
| Add | -4 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Firerate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.8 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Permutations/BP_Item_AssaultRifle_Pneumatic_01_XRounds.json |
| Item | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Permutations/DA_Item_AssaultRifle_Pneumatic_01_XRounds.json |
| Quality set | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_WeaponQualitySet_AssaultRifle_Pneumatic_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_WeaponQualitySet_AssaultRifle_Pneumatic_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/BP_Projectile_AssaultRifle_Pneumatic_01_XRounds.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Permutations/BP_Item_AssaultRifle_Pneumatic_01_XRounds.json, Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_Item_AssaultRifle_Pneumatic_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | AssaultRifle_Pneumatic_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_Pneumatic_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

<details>
<summary>Actual game source files</summary>

- [Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/BP_Item_AssaultRifle_Pneumatic_01_Ascended.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/BP_Item_AssaultRifle_Pneumatic_01_Ascended.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/BP_Projectile_AssaultRifle_Pneumatic_01_AntiShield.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/BP_Projectile_AssaultRifle_Pneumatic_01_AntiShield.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/BP_Projectile_AssaultRifle_Pneumatic_01_XRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/BP_Projectile_AssaultRifle_Pneumatic_01_XRounds.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/DA_Item_AssaultRifle_Pneumatic_01_Ascended.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/DA_Item_AssaultRifle_Pneumatic_01_Ascended.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Permutations/BP_Item_AssaultRifle_Pneumatic_01_AntiShield.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Permutations/BP_Item_AssaultRifle_Pneumatic_01_AntiShield.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Permutations/BP_Item_AssaultRifle_Pneumatic_01_AntiShield_FullAuto.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Permutations/BP_Item_AssaultRifle_Pneumatic_01_AntiShield_FullAuto.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Permutations/BP_Item_AssaultRifle_Pneumatic_01_FullAuto.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Permutations/BP_Item_AssaultRifle_Pneumatic_01_FullAuto.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Permutations/BP_Item_AssaultRifle_Pneumatic_01_XRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Permutations/BP_Item_AssaultRifle_Pneumatic_01_XRounds.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Permutations/DA_Item_AssaultRifle_Pneumatic_01_AntiShield.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Permutations/DA_Item_AssaultRifle_Pneumatic_01_AntiShield.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Permutations/DA_Item_AssaultRifle_Pneumatic_01_AntiShield_FullAuto.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Permutations/DA_Item_AssaultRifle_Pneumatic_01_AntiShield_FullAuto.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Permutations/DA_Item_AssaultRifle_Pneumatic_01_FullAuto.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Permutations/DA_Item_AssaultRifle_Pneumatic_01_FullAuto.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Permutations/DA_Item_AssaultRifle_Pneumatic_01_XRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Permutations/DA_Item_AssaultRifle_Pneumatic_01_XRounds.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_Pneumatic_01_AntiShield.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_Pneumatic_01_AntiShield.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_Pneumatic_01_FullAuto.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_Pneumatic_01_FullAuto.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_Pneumatic_01_XRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_Pneumatic_01_XRounds.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_Pneumatic_01_AntiShield.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_Pneumatic_01_AntiShield.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_Pneumatic_01_Ascended.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_Pneumatic_01_Ascended.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_Pneumatic_01_FullAuto.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_Pneumatic_01_FullAuto.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_Pneumatic_01_XRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_Pneumatic_01_XRounds.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_Item_AssaultRifle_Pneumatic_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_Item_AssaultRifle_Pneumatic_01.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_Projectile_AssaultRifle_Pneumatic_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_Projectile_AssaultRifle_Pneumatic_01.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_WeaponQualitySet_AssaultRifle_Pneumatic_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/BP_WeaponQualitySet_AssaultRifle_Pneumatic_01.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Curve_DamageFalloff_AssaultRifle_Pneumatic_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/Curve_DamageFalloff_AssaultRifle_Pneumatic_01.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/DA_Item_AssaultRifle_Pneumatic_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Pneumatic_01/DA_Item_AssaultRifle_Pneumatic_01.json)

</details>
