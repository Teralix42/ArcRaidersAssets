[Weapon index](README.md) · [Definitions and mechanics](Mechanics.md) · [JSON data](weapons.json)

# Osprey

Internal weapon id: `SniperRifle_BoltAction_Medium_01`. Ammo: **MediumAmmo**.

### Standard levels

| Level / variant | Damage / projectile | Projectiles | Full spread | Crit × | ARC armour × | ARC weakpoint × | RPM | Magazine | Reload stat, s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I | 45 | 1 | 45 | 2 | 0.8 | 1 | 45 | 8 | 4 |
| II | 45 | 1 | 45 | 2 | 0.8 | 1 | 45 | 8 | 3.5 |
| III | 45 | 1 | 45 | 2 | 0.8 | 1 | 45 | 8 | 3 |
| IV | 45 | 1 | 45 | 2 | 0.8 | 1 | 45 | 8 | 2.5 |

#### Level I

| Identity | Value |
| --- | --- |
| Id | SniperRifle_BoltAction_Medium_01_Level1 |
| Level | 1 |
| Level label | I |
| Variant | Standard |
| Quality index | 0 |
| Uses standard level | 1 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 45 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 45 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 0.8 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 45 |
| Firing mode | BoltAction |
| Burst size stat | 1 |
| Magazine size | 8 |
| Reload time stat, seconds | 4 |
| Cooldown time stat, seconds | 1.5 |
| Durability burn rate stat | 0.008775 |
| Base partial-reload duration, seconds | 2.8 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 45 | 45 |
| Armor | 0.6 | 0.4 | 0.8 | 1 | 0.32 | 14.4 | 14.4 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 18 | 18 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 67.5 | 67.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 67.5 | 67.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 54 | 54 |

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
| Damage | 45 |
| Fire rate | 7.357 |
| Range | 79.121 |
| Stability | 79.035 |
| Agility | 54.082 |
| Stealth | 12 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Curve_DamageFalloff_SniperRifle_BoltAction_Medium_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 17,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.3 |
| Multiply | 1 |

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | 0.5 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_Item_SniperRifle_BoltAction_Medium_01.json |
| Item | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/DA_Item_SniperRifle_BoltAction_Medium_01.json |
| Quality set | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_WeaponQualitySet_SniperRifle_BoltAction_Medium_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_WeaponQualitySet_SniperRifle_BoltAction_Medium_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_Projectile_SniperRifle_BoltAction_Medium_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Shared/BaseClasses/SniperRifle_Base/BP_Item_SniperRifle_Base.json, Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_Item_SniperRifle_BoltAction_Medium_01.json

#### Level II

| Identity | Value |
| --- | --- |
| Id | SniperRifle_BoltAction_Medium_01_Level2 |
| Level | 2 |
| Level label | II |
| Variant | Standard |
| Quality index | 1 |
| Uses standard level | 2 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 45 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 45 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 0.8 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 45 |
| Firing mode | BoltAction |
| Burst size stat | 1 |
| Magazine size | 8 |
| Reload time stat, seconds | 3.5 |
| Cooldown time stat, seconds | 1.4 |
| Durability burn rate stat | 0.00675 |
| Base partial-reload duration, seconds | 2.8 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 45 | 45 |
| Armor | 0.6 | 0.4 | 0.8 | 1 | 0.32 | 14.4 | 14.4 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 18 | 18 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 67.5 | 67.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 67.5 | 67.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 54 | 54 |

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
| Damage | 45 |
| Fire rate | 7.857 |
| Range | 79.121 |
| Stability | 79.035 |
| Agility | 55.582 |
| Stealth | 12 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Curve_DamageFalloff_SniperRifle_BoltAction_Medium_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 17,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Cooldowntime

| Field | Value |
| --- | --- |
| Add | -0.1 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_Item_SniperRifle_BoltAction_Medium_01.json |
| Item | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/DA_Item_SniperRifle_BoltAction_Medium_01.json |
| Quality set | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_WeaponQualitySet_SniperRifle_BoltAction_Medium_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_WeaponQualitySet_SniperRifle_BoltAction_Medium_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_Projectile_SniperRifle_BoltAction_Medium_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Shared/BaseClasses/SniperRifle_Base/BP_Item_SniperRifle_Base.json, Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_Item_SniperRifle_BoltAction_Medium_01.json

#### Level III

| Identity | Value |
| --- | --- |
| Id | SniperRifle_BoltAction_Medium_01_Level3 |
| Level | 3 |
| Level label | III |
| Variant | Standard |
| Quality index | 2 |
| Uses standard level | 3 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 45 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 45 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 0.8 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 45 |
| Firing mode | BoltAction |
| Burst size stat | 1 |
| Magazine size | 8 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 1.3 |
| Durability burn rate stat | 0.004725 |
| Base partial-reload duration, seconds | 2.8 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 45 | 45 |
| Armor | 0.6 | 0.4 | 0.8 | 1 | 0.32 | 14.4 | 14.4 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 18 | 18 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 67.5 | 67.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 67.5 | 67.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 54 | 54 |

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
| Damage | 45 |
| Fire rate | 8.357 |
| Range | 79.121 |
| Stability | 79.035 |
| Agility | 56.582 |
| Stealth | 12 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Curve_DamageFalloff_SniperRifle_BoltAction_Medium_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 17,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Cooldowntime

| Field | Value |
| --- | --- |
| Add | -0.2 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
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
| Weapon | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_Item_SniperRifle_BoltAction_Medium_01.json |
| Item | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/DA_Item_SniperRifle_BoltAction_Medium_01.json |
| Quality set | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_WeaponQualitySet_SniperRifle_BoltAction_Medium_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_WeaponQualitySet_SniperRifle_BoltAction_Medium_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_Projectile_SniperRifle_BoltAction_Medium_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Shared/BaseClasses/SniperRifle_Base/BP_Item_SniperRifle_Base.json, Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_Item_SniperRifle_BoltAction_Medium_01.json

#### Level IV

| Identity | Value |
| --- | --- |
| Id | SniperRifle_BoltAction_Medium_01_Level4 |
| Level | 4 |
| Level label | IV |
| Variant | Standard |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 45 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 45 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 0.8 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 45 |
| Firing mode | BoltAction |
| Burst size stat | 1 |
| Magazine size | 8 |
| Reload time stat, seconds | 2.5 |
| Cooldown time stat, seconds | 1.2 |
| Durability burn rate stat | 0.0027 |
| Base partial-reload duration, seconds | 2.8 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 45 | 45 |
| Armor | 0.6 | 0.4 | 0.8 | 1 | 0.32 | 14.4 | 14.4 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 18 | 18 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 67.5 | 67.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 67.5 | 67.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 54 | 54 |

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
| Damage | 45 |
| Fire rate | 8.357 |
| Range | 79.121 |
| Stability | 79.035 |
| Agility | 56.582 |
| Stealth | 12 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Curve_DamageFalloff_SniperRifle_BoltAction_Medium_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 17,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Cooldowntime

| Field | Value |
| --- | --- |
| Add | -0.3 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.4 |
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
| Weapon | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_Item_SniperRifle_BoltAction_Medium_01.json |
| Item | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/DA_Item_SniperRifle_BoltAction_Medium_01.json |
| Quality set | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_WeaponQualitySet_SniperRifle_BoltAction_Medium_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_WeaponQualitySet_SniperRifle_BoltAction_Medium_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_Projectile_SniperRifle_BoltAction_Medium_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Shared/BaseClasses/SniperRifle_Base/BP_Item_SniperRifle_Base.json, Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_Item_SniperRifle_BoltAction_Medium_01.json

### Amplified configurations

| Level / variant | Damage / projectile | Projectiles | Full spread | Crit × | ARC armour × | ARC weakpoint × | RPM | Magazine | Reload stat, s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Default | 45 | 1 | 45 | 2 | 0.8 | 1 | 45 | 8 | 2.5 |
| Anti-Weak Point | 45 | 1 | 45 | 2 | 0.8 | 2 | 45 | 8 | 2.5 |
| Ergonomic Bolt | 45 | 1 | 45 | 2 | 0.8 | 1 | 45 | 8 | 2.5 |
| Ergonomic Bolt + Anti-Weak Point | 45 | 1 | 45 | 2 | 0.8 | 2 | 45 | 8 | 2.5 |
| Tracker Rounds | 45 | 1 | 45 | 2 | 0.8 | 1 | 45 | 8 | 2.5 |
| Tracker Rounds + Ergonomic Bolt | 45 | 1 | 45 | 2 | 0.8 | 1 | 45 | 8 | 2.5 |

#### Amplified — Default

| Identity | Value |
| --- | --- |
| Id | SniperRifle_BoltAction_Medium_01_Ascended |
| Level | 5 |
| Level label | Amplified |
| Variant | Default |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 45 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 45 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 0.8 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 45 |
| Firing mode | BoltAction |
| Burst size stat | 1 |
| Magazine size | 8 |
| Reload time stat, seconds | 2.5 |
| Cooldown time stat, seconds | 1.2 |
| Durability burn rate stat | 0.00135 |
| Base partial-reload duration, seconds | 2.8 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 45 | 45 |
| Armor | 0.6 | 0.4 | 0.8 | 1 | 0.32 | 14.4 | 14.4 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 18 | 18 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 67.5 | 67.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 67.5 | 67.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 54 | 54 |

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
| Damage | 45 |
| Fire rate | 8.357 |
| Range | 79.121 |
| Stability | 79.035 |
| Agility | 56.582 |
| Stealth | 12 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Curve_DamageFalloff_SniperRifle_BoltAction_Medium_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 17,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Cooldowntime

| Field | Value |
| --- | --- |
| Add | -0.3 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.4 |
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
| Weapon | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/BP_Item_SniperRifle_BoltAction_Medium_01_Ascended.json |
| Item | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/DA_Item_SniperRifle_BoltAction_Medium_01_Ascended.json |
| Quality set | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_WeaponQualitySet_SniperRifle_BoltAction_Medium_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_WeaponQualitySet_SniperRifle_BoltAction_Medium_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_Projectile_SniperRifle_BoltAction_Medium_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Shared/BaseClasses/SniperRifle_Base/BP_Item_SniperRifle_Base.json, Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_Item_SniperRifle_BoltAction_Medium_01.json

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | SniperRifle_BoltAction_Medium_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/DA_Upgrade_SniperRifle_BoltAction_Medium_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Anti-Weak Point

| Identity | Value |
| --- | --- |
| Id | SniperRifle_BoltAction_Medium_01_AntiWeakPoint |
| Level | 5 |
| Level label | Amplified |
| Variant | Anti-Weak Point |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 45 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 45 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 0.8 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 2 |
| Fire rate stat, RPM | 45 |
| Firing mode | BoltAction |
| Burst size stat | 1 |
| Magazine size | 8 |
| Reload time stat, seconds | 2.5 |
| Cooldown time stat, seconds | 1.2 |
| Durability burn rate stat | 0.00135 |
| Base partial-reload duration, seconds | 2.8 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 45 | 45 |
| Armor | 0.6 | 0.4 | 0.8 | 1 | 0.32 | 14.4 | 14.4 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 18 | 18 |
| WeakPoint | -0.5 | 1.5 | 1 | 2 | 3 | 135 | 135 |
| Critical | -0.5 | 1.5 | 1 | 2 | 3 | 135 | 135 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 54 | 54 |

##### Upgrades

###### Anti-Weak Point

| Field | Value |
| --- | --- |
| Id | SniperRifle_BoltAction_Medium_01_AntiWeakPoint |
| Name | Anti-Weak Point |
| Description | Deals increased damage to ARC weak points, but deals less damage to ARC armor plating. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/DA_Upgrade_SniperRifle_BoltAction_Medium_01_AntiWeakPoint.json |
| Modifier source path | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/BP_UpgradeWeaponMod_SniperRifle_BoltAction_Medium_01_AntiWeakPoint.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/BP_UpgradeWeaponMod_SniperRifle_BoltAction_Medium_01_AntiWeakPoint.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Aiweakspotdamagemultiplier**

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
| Damage | 45 |
| Fire rate | 8.357 |
| Range | 79.121 |
| Stability | 79.035 |
| Agility | 56.582 |
| Stealth | 12 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Curve_DamageFalloff_SniperRifle_BoltAction_Medium_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 17,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Cooldowntime

| Field | Value |
| --- | --- |
| Add | -0.3 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.4 |
| Multiply | 1 |

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | -1 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Aiweakspotdamagemultiplier

| Field | Value |
| --- | --- |
| Add | 1 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Permutations/BP_Item_SniperRifle_BoltAction_Medium_01_AntiWeakPoint.json |
| Item | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Permutations/DA_Item_SniperRifle_BoltAction_Medium_01_AntiWeakPoint.json |
| Quality set | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_WeaponQualitySet_SniperRifle_BoltAction_Medium_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_WeaponQualitySet_SniperRifle_BoltAction_Medium_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_Projectile_SniperRifle_BoltAction_Medium_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Shared/BaseClasses/SniperRifle_Base/BP_Item_SniperRifle_Base.json, Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_Item_SniperRifle_BoltAction_Medium_01.json

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | SniperRifle_BoltAction_Medium_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/DA_Upgrade_SniperRifle_BoltAction_Medium_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Ergonomic Bolt

| Identity | Value |
| --- | --- |
| Id | SniperRifle_BoltAction_Medium_01_StraightBolt |
| Level | 5 |
| Level label | Amplified |
| Variant | Ergonomic Bolt |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 45 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 45 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 0.8 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 45 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 8 |
| Reload time stat, seconds | 2.5 |
| Cooldown time stat, seconds | 1.2 |
| Durability burn rate stat | 0.00135 |
| Base partial-reload duration, seconds | 2.8 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 45 | 45 |
| Armor | 0.6 | 0.4 | 0.8 | 1 | 0.32 | 14.4 | 14.4 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 18 | 18 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 67.5 | 67.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 67.5 | 67.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 54 | 54 |

##### Upgrades

###### Ergonomic Bolt

| Field | Value |
| --- | --- |
| Id | SniperRifle_BoltAction_Medium_01_StraightBolt |
| Name | Ergonomic Bolt |
| Description | Ergonomic bolt that allows the user to perform the bolt-action while scoped. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/DA_Upgrade_SniperRifle_BoltAction_Medium_01_StraightBolt.json |
| Modifier source path | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/BP_UpgradeWeaponMod_SniperRifle_BoltAction_Medium_01_StraightBolt.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/BP_UpgradeWeaponMod_SniperRifle_BoltAction_Medium_01_StraightBolt.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Firingmodeoverride**

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Currentfiringmode | EFiringMode::SemiAuto |

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

None.

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 45 |
| Fire rate | 10.5 |
| Range | 79.121 |
| Stability | 79.035 |
| Agility | 56.582 |
| Stealth | 12 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Curve_DamageFalloff_SniperRifle_BoltAction_Medium_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 17,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Cooldowntime

| Field | Value |
| --- | --- |
| Add | -0.3 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.4 |
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
| Currentfiringmode | EFiringMode::SemiAuto |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Permutations/BP_Item_SniperRifle_BoltAction_Medium_01_StraightBolt.json |
| Item | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Permutations/DA_Item_SniperRifle_BoltAction_Medium_01_StraightBolt.json |
| Quality set | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_WeaponQualitySet_SniperRifle_BoltAction_Medium_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_WeaponQualitySet_SniperRifle_BoltAction_Medium_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_Projectile_SniperRifle_BoltAction_Medium_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Shared/BaseClasses/SniperRifle_Base/BP_Item_SniperRifle_Base.json, Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_Item_SniperRifle_BoltAction_Medium_01.json

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | SniperRifle_BoltAction_Medium_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/DA_Upgrade_SniperRifle_BoltAction_Medium_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Ergonomic Bolt + Anti-Weak Point

| Identity | Value |
| --- | --- |
| Id | SniperRifle_BoltAction_Medium_01_StraightBolt_AntiWeakPoint |
| Level | 5 |
| Level label | Amplified |
| Variant | Ergonomic Bolt + Anti-Weak Point |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 45 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 45 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 0.8 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 2 |
| Fire rate stat, RPM | 45 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 8 |
| Reload time stat, seconds | 2.5 |
| Cooldown time stat, seconds | 1.2 |
| Durability burn rate stat | 0.00135 |
| Base partial-reload duration, seconds | 2.8 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 45 | 45 |
| Armor | 0.6 | 0.4 | 0.8 | 1 | 0.32 | 14.4 | 14.4 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 18 | 18 |
| WeakPoint | -0.5 | 1.5 | 1 | 2 | 3 | 135 | 135 |
| Critical | -0.5 | 1.5 | 1 | 2 | 3 | 135 | 135 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 54 | 54 |

##### Upgrades

###### Ergonomic Bolt

| Field | Value |
| --- | --- |
| Id | SniperRifle_BoltAction_Medium_01_StraightBolt |
| Name | Ergonomic Bolt |
| Description | Ergonomic bolt that allows the user to perform the bolt-action while scoped. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/DA_Upgrade_SniperRifle_BoltAction_Medium_01_StraightBolt.json |
| Modifier source path | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/BP_UpgradeWeaponMod_SniperRifle_BoltAction_Medium_01_StraightBolt.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/BP_UpgradeWeaponMod_SniperRifle_BoltAction_Medium_01_StraightBolt.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Firingmodeoverride**

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Currentfiringmode | EFiringMode::SemiAuto |

###### Anti-Weak Point

| Field | Value |
| --- | --- |
| Id | SniperRifle_BoltAction_Medium_01_AntiWeakPoint |
| Name | Anti-Weak Point |
| Description | Deals increased damage to ARC weak points, but deals less damage to ARC armor plating. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/DA_Upgrade_SniperRifle_BoltAction_Medium_01_AntiWeakPoint.json |
| Modifier source path | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/BP_UpgradeWeaponMod_SniperRifle_BoltAction_Medium_01_AntiWeakPoint.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/BP_UpgradeWeaponMod_SniperRifle_BoltAction_Medium_01_AntiWeakPoint.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Aiweakspotdamagemultiplier**

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
| Damage | 45 |
| Fire rate | 10.5 |
| Range | 79.121 |
| Stability | 79.035 |
| Agility | 56.582 |
| Stealth | 12 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Curve_DamageFalloff_SniperRifle_BoltAction_Medium_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 17,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Cooldowntime

| Field | Value |
| --- | --- |
| Add | -0.3 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.4 |
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
| Currentfiringmode | EFiringMode::SemiAuto |

###### Aiweakspotdamagemultiplier

| Field | Value |
| --- | --- |
| Add | 1 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Permutations/BP_Item_SniperRifle_BoltAction_Medium_01_StraightBolt_AntiWeakPoint.json |
| Item | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Permutations/DA_Item_SniperRifle_BoltAction_Medium_01_StraightBolt_AntiWeakPoint.json |
| Quality set | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_WeaponQualitySet_SniperRifle_BoltAction_Medium_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_WeaponQualitySet_SniperRifle_BoltAction_Medium_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_Projectile_SniperRifle_BoltAction_Medium_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Shared/BaseClasses/SniperRifle_Base/BP_Item_SniperRifle_Base.json, Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_Item_SniperRifle_BoltAction_Medium_01.json

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | SniperRifle_BoltAction_Medium_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/DA_Upgrade_SniperRifle_BoltAction_Medium_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Tracker Rounds

| Identity | Value |
| --- | --- |
| Id | SniperRifle_BoltAction_Medium_01_TrackerRounds |
| Level | 5 |
| Level label | Amplified |
| Variant | Tracker Rounds |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 45 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 45 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 0.8 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 45 |
| Firing mode | BoltAction |
| Burst size stat | 1 |
| Magazine size | 8 |
| Reload time stat, seconds | 2.5 |
| Cooldown time stat, seconds | 1.2 |
| Durability burn rate stat | 0.00135 |
| Base partial-reload duration, seconds | 2.8 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 45 | 45 |
| Armor | 0.6 | 0.4 | 0.8 | 1 | 0.32 | 14.4 | 14.4 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 18 | 18 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 67.5 | 67.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 67.5 | 67.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 54 | 54 |

##### Upgrades

###### Tracker Rounds

| Field | Value |
| --- | --- |
| Id | SniperRifle_BoltAction_Medium_01_TrackerRounds |
| Name | Tracker Rounds |
| Description | Replaces the bullets with tracker rounds that briefly reveal the position of targets they hit. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/DA_Upgrade_SniperRifle_BoltAction_Medium_01_TrackerRounds.json |
| Modifier source path | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/BP_UpgradeWeaponMod_SniperRifle_BoltAction_Medium_01_TrackerRounds.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/BP_UpgradeWeaponMod_SniperRifle_BoltAction_Medium_01_TrackerRounds.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Launchspeed**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.4 |
| Multiply | 1 |

**Taggingtime**

| Field | Value |
| --- | --- |
| Add | 5 |
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
| Damage | 45 |
| Fire rate | 8.357 |
| Range | 65 |
| Stability | 79.035 |
| Agility | 56.582 |
| Stealth | 12 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Curve_DamageFalloff_SniperRifle_BoltAction_Medium_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 17,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Cooldowntime

| Field | Value |
| --- | --- |
| Add | -0.3 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.4 |
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
| Add | 0 |
| Addmultiply | 0.4 |
| Multiply | 1 |

###### Taggingtime

| Field | Value |
| --- | --- |
| Add | 5 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Permutations/BP_Item_SniperRifle_BoltAction_Medium_01_TrackerRounds.json |
| Item | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Permutations/DA_Item_SniperRifle_BoltAction_Medium_01_TrackerRounds.json |
| Quality set | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_WeaponQualitySet_SniperRifle_BoltAction_Medium_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_WeaponQualitySet_SniperRifle_BoltAction_Medium_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_Projectile_SniperRifle_BoltAction_Medium_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Shared/BaseClasses/SniperRifle_Base/BP_Item_SniperRifle_Base.json, Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_Item_SniperRifle_BoltAction_Medium_01.json

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | SniperRifle_BoltAction_Medium_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/DA_Upgrade_SniperRifle_BoltAction_Medium_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Tracker Rounds + Ergonomic Bolt

| Identity | Value |
| --- | --- |
| Id | SniperRifle_BoltAction_Medium_01_TrackerRounds_StraightBolt |
| Level | 5 |
| Level label | Amplified |
| Variant | Tracker Rounds + Ergonomic Bolt |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 45 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 45 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 0.8 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 45 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 8 |
| Reload time stat, seconds | 2.5 |
| Cooldown time stat, seconds | 1.2 |
| Durability burn rate stat | 0.00135 |
| Base partial-reload duration, seconds | 2.8 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 45 | 45 |
| Armor | 0.6 | 0.4 | 0.8 | 1 | 0.32 | 14.4 | 14.4 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 18 | 18 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 67.5 | 67.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 67.5 | 67.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 54 | 54 |

##### Upgrades

###### Tracker Rounds

| Field | Value |
| --- | --- |
| Id | SniperRifle_BoltAction_Medium_01_TrackerRounds |
| Name | Tracker Rounds |
| Description | Replaces the bullets with tracker rounds that briefly reveal the position of targets they hit. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/DA_Upgrade_SniperRifle_BoltAction_Medium_01_TrackerRounds.json |
| Modifier source path | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/BP_UpgradeWeaponMod_SniperRifle_BoltAction_Medium_01_TrackerRounds.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/BP_UpgradeWeaponMod_SniperRifle_BoltAction_Medium_01_TrackerRounds.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Launchspeed**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.4 |
| Multiply | 1 |

**Taggingtime**

| Field | Value |
| --- | --- |
| Add | 5 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Ergonomic Bolt

| Field | Value |
| --- | --- |
| Id | SniperRifle_BoltAction_Medium_01_StraightBolt |
| Name | Ergonomic Bolt |
| Description | Ergonomic bolt that allows the user to perform the bolt-action while scoped. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/DA_Upgrade_SniperRifle_BoltAction_Medium_01_StraightBolt.json |
| Modifier source path | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/BP_UpgradeWeaponMod_SniperRifle_BoltAction_Medium_01_StraightBolt.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/BP_UpgradeWeaponMod_SniperRifle_BoltAction_Medium_01_StraightBolt.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Firingmodeoverride**

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Currentfiringmode | EFiringMode::SemiAuto |

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

None.

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 45 |
| Fire rate | 10.5 |
| Range | 65 |
| Stability | 79.035 |
| Agility | 56.582 |
| Stealth | 12 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Curve_DamageFalloff_SniperRifle_BoltAction_Medium_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 17,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Cooldowntime

| Field | Value |
| --- | --- |
| Add | -0.3 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.4 |
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
| Add | 0 |
| Addmultiply | 0.4 |
| Multiply | 1 |

###### Taggingtime

| Field | Value |
| --- | --- |
| Add | 5 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Firingmodeoverride

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Currentfiringmode | EFiringMode::SemiAuto |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Permutations/BP_Item_SniperRifle_BoltAction_Medium_01_TrackerRounds_StraightBolt.json |
| Item | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Permutations/DA_Item_SniperRifle_BoltAction_Medium_01_TrackerRounds_StraightBolt.json |
| Quality set | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_WeaponQualitySet_SniperRifle_BoltAction_Medium_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_WeaponQualitySet_SniperRifle_BoltAction_Medium_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_Projectile_SniperRifle_BoltAction_Medium_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Shared/BaseClasses/SniperRifle_Base/BP_Item_SniperRifle_Base.json, Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_Item_SniperRifle_BoltAction_Medium_01.json

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | SniperRifle_BoltAction_Medium_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/DA_Upgrade_SniperRifle_BoltAction_Medium_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

<details>
<summary>Actual game source files</summary>

- [Content/Pioneer/Items/Firearms/Shared/BaseClasses/SniperRifle_Base/BP_Item_SniperRifle_Base.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shared/BaseClasses/SniperRifle_Base/BP_Item_SniperRifle_Base.json)
- [Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/BP_Item_SniperRifle_BoltAction_Medium_01_Ascended.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/BP_Item_SniperRifle_BoltAction_Medium_01_Ascended.json)
- [Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/DA_Item_SniperRifle_BoltAction_Medium_01_Ascended.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/DA_Item_SniperRifle_BoltAction_Medium_01_Ascended.json)
- [Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Permutations/BP_Item_SniperRifle_BoltAction_Medium_01_AntiWeakPoint.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Permutations/BP_Item_SniperRifle_BoltAction_Medium_01_AntiWeakPoint.json)
- [Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Permutations/BP_Item_SniperRifle_BoltAction_Medium_01_StraightBolt.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Permutations/BP_Item_SniperRifle_BoltAction_Medium_01_StraightBolt.json)
- [Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Permutations/BP_Item_SniperRifle_BoltAction_Medium_01_StraightBolt_AntiWeakPoint.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Permutations/BP_Item_SniperRifle_BoltAction_Medium_01_StraightBolt_AntiWeakPoint.json)
- [Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Permutations/BP_Item_SniperRifle_BoltAction_Medium_01_TrackerRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Permutations/BP_Item_SniperRifle_BoltAction_Medium_01_TrackerRounds.json)
- [Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Permutations/BP_Item_SniperRifle_BoltAction_Medium_01_TrackerRounds_StraightBolt.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Permutations/BP_Item_SniperRifle_BoltAction_Medium_01_TrackerRounds_StraightBolt.json)
- [Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Permutations/DA_Item_SniperRifle_BoltAction_Medium_01_AntiWeakPoint.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Permutations/DA_Item_SniperRifle_BoltAction_Medium_01_AntiWeakPoint.json)
- [Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Permutations/DA_Item_SniperRifle_BoltAction_Medium_01_StraightBolt.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Permutations/DA_Item_SniperRifle_BoltAction_Medium_01_StraightBolt.json)
- [Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Permutations/DA_Item_SniperRifle_BoltAction_Medium_01_StraightBolt_AntiWeakPoint.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Permutations/DA_Item_SniperRifle_BoltAction_Medium_01_StraightBolt_AntiWeakPoint.json)
- [Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Permutations/DA_Item_SniperRifle_BoltAction_Medium_01_TrackerRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Permutations/DA_Item_SniperRifle_BoltAction_Medium_01_TrackerRounds.json)
- [Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Permutations/DA_Item_SniperRifle_BoltAction_Medium_01_TrackerRounds_StraightBolt.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Permutations/DA_Item_SniperRifle_BoltAction_Medium_01_TrackerRounds_StraightBolt.json)
- [Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/BP_UpgradeWeaponMod_SniperRifle_BoltAction_Medium_01_AntiWeakPoint.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/BP_UpgradeWeaponMod_SniperRifle_BoltAction_Medium_01_AntiWeakPoint.json)
- [Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/BP_UpgradeWeaponMod_SniperRifle_BoltAction_Medium_01_StraightBolt.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/BP_UpgradeWeaponMod_SniperRifle_BoltAction_Medium_01_StraightBolt.json)
- [Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/BP_UpgradeWeaponMod_SniperRifle_BoltAction_Medium_01_TrackerRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/BP_UpgradeWeaponMod_SniperRifle_BoltAction_Medium_01_TrackerRounds.json)
- [Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/DA_Upgrade_SniperRifle_BoltAction_Medium_01_AntiWeakPoint.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/DA_Upgrade_SniperRifle_BoltAction_Medium_01_AntiWeakPoint.json)
- [Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/DA_Upgrade_SniperRifle_BoltAction_Medium_01_Ascended.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/DA_Upgrade_SniperRifle_BoltAction_Medium_01_Ascended.json)
- [Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/DA_Upgrade_SniperRifle_BoltAction_Medium_01_StraightBolt.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/DA_Upgrade_SniperRifle_BoltAction_Medium_01_StraightBolt.json)
- [Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/DA_Upgrade_SniperRifle_BoltAction_Medium_01_TrackerRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/DA_Upgrade_SniperRifle_BoltAction_Medium_01_TrackerRounds.json)
- [Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_Item_SniperRifle_BoltAction_Medium_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_Item_SniperRifle_BoltAction_Medium_01.json)
- [Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_Projectile_SniperRifle_BoltAction_Medium_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_Projectile_SniperRifle_BoltAction_Medium_01.json)
- [Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_WeaponQualitySet_SniperRifle_BoltAction_Medium_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_WeaponQualitySet_SniperRifle_BoltAction_Medium_01.json)
- [Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Curve_DamageFalloff_SniperRifle_BoltAction_Medium_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Curve_DamageFalloff_SniperRifle_BoltAction_Medium_01.json)
- [Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/DA_Item_SniperRifle_BoltAction_Medium_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/DA_Item_SniperRifle_BoltAction_Medium_01.json)

</details>
