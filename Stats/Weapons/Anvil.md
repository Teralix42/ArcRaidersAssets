[Weapon index](README.md) · [Definitions and mechanics](Mechanics.md) · [JSON data](weapons.json)

# Anvil

Internal weapon id: `HandCannon_SingleAction_01`. Ammo: **HeavyAmmo**.

### Standard levels

| Level / variant | Damage / projectile | Projectiles | Full spread | Crit × | ARC armour × | ARC weakpoint × | RPM | Magazine | Reload stat, s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I | 40 | 1 | 40 | 2.5 | 1.5 | 1 | 40 | 6 | 2.5 |
| II | 40 | 1 | 40 | 2.5 | 1.5 | 1 | 50 | 6 | 2.5 |
| III | 40 | 1 | 40 | 2.5 | 1.5 | 1 | 60 | 6 | 2.5 |
| IV | 40 | 1 | 40 | 2.5 | 1.5 | 1 | 70 | 6 | 2.5 |

#### Level I

| Identity | Value |
| --- | --- |
| Id | HandCannon_SingleAction_01_Level1 |
| Level | 1 |
| Level label | I |
| Variant | Standard |
| Quality index | 0 |
| Uses standard level | 1 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 40 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 40 |
| Firearm critical/headshot multiplier | 2.5 |
| ARC armour multiplier | 1.5 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 40 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 6 |
| Reload time stat, seconds | 2.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.005333 |
| Base partial-reload duration, seconds | — |
| Uses shell/looping reload | Yes |
| Base shell-reload entry, seconds | 0.8 |
| Base shell-reload loop, seconds | 0.7 |
| Base shell-reload exit, seconds | 0.55 |
| Shells loaded per loop | 1 |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 40 | 40 |
| Armor | 0.6 | 0.4 | 1.5 | 1 | 0.6 | 24 | 24 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 16 | 16 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 60 | 60 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 60 | 60 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 48 | 48 |

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
| Damage | 40 |
| Fire rate | 7.333 |
| Range | 50.21 |
| Stability | 79.769 |
| Agility | 68.605 |
| Stealth | 10 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Curve_DamageFalloff_HandCannon_SingleAction_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 18,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 20,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Firerate

| Field | Value |
| --- | --- |
| Add | -10 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Dispersionrecoveryspeed

| Field | Value |
| --- | --- |
| Add | 0.25 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/BP_Item_HandCannon_SingleAction_01.json |
| Item | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/DA_Item_HandCannon_SingleAction_01.json |
| Quality set | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/BP_WeaponQualitySet_HandCannon_SingleAction_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/BP_WeaponQualitySet_HandCannon_SingleAction_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/BP_Projectile_HandCannon_SingleAction_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/BP_Item_HandCannon_SingleAction_01.json, Script/PrecompiledScript.Cache

#### Level II

| Identity | Value |
| --- | --- |
| Id | HandCannon_SingleAction_01_Level2 |
| Level | 2 |
| Level label | II |
| Variant | Standard |
| Quality index | 1 |
| Uses standard level | 2 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 40 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 40 |
| Firearm critical/headshot multiplier | 2.5 |
| ARC armour multiplier | 1.5 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 50 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 6 |
| Reload time stat, seconds | 2.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.0048 |
| Base partial-reload duration, seconds | — |
| Uses shell/looping reload | Yes |
| Base shell-reload entry, seconds | 0.8 |
| Base shell-reload loop, seconds | 0.7 |
| Base shell-reload exit, seconds | 0.55 |
| Shells loaded per loop | 1 |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 40 | 40 |
| Armor | 0.6 | 0.4 | 1.5 | 1 | 0.6 | 24 | 24 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 16 | 16 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 60 | 60 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 60 | 60 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 48 | 48 |

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
| Damage | 40 |
| Fire rate | 8.333 |
| Range | 50.21 |
| Stability | 75.769 |
| Agility | 69.105 |
| Stealth | 10 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Curve_DamageFalloff_HandCannon_SingleAction_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
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
| Weapon | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/BP_Item_HandCannon_SingleAction_01.json |
| Item | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/DA_Item_HandCannon_SingleAction_01.json |
| Quality set | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/BP_WeaponQualitySet_HandCannon_SingleAction_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/BP_WeaponQualitySet_HandCannon_SingleAction_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/BP_Projectile_HandCannon_SingleAction_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/BP_Item_HandCannon_SingleAction_01.json, Script/PrecompiledScript.Cache

#### Level III

| Identity | Value |
| --- | --- |
| Id | HandCannon_SingleAction_01_Level3 |
| Level | 3 |
| Level label | III |
| Variant | Standard |
| Quality index | 2 |
| Uses standard level | 3 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 40 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 40 |
| Firearm critical/headshot multiplier | 2.5 |
| ARC armour multiplier | 1.5 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 60 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 6 |
| Reload time stat, seconds | 2.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.004266 |
| Base partial-reload duration, seconds | — |
| Uses shell/looping reload | Yes |
| Base shell-reload entry, seconds | 0.8 |
| Base shell-reload loop, seconds | 0.7 |
| Base shell-reload exit, seconds | 0.55 |
| Shells loaded per loop | 1 |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 40 | 40 |
| Armor | 0.6 | 0.4 | 1.5 | 1 | 0.6 | 24 | 24 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 16 | 16 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 60 | 60 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 60 | 60 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 48 | 48 |

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
| Damage | 40 |
| Fire rate | 9.333 |
| Range | 50.21 |
| Stability | 71.769 |
| Agility | 69.605 |
| Stealth | 10 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Curve_DamageFalloff_HandCannon_SingleAction_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
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

###### Firerate

| Field | Value |
| --- | --- |
| Add | 10 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Dispersionrecoveryspeed

| Field | Value |
| --- | --- |
| Add | -0.25 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/BP_Item_HandCannon_SingleAction_01.json |
| Item | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/DA_Item_HandCannon_SingleAction_01.json |
| Quality set | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/BP_WeaponQualitySet_HandCannon_SingleAction_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/BP_WeaponQualitySet_HandCannon_SingleAction_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/BP_Projectile_HandCannon_SingleAction_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/BP_Item_HandCannon_SingleAction_01.json, Script/PrecompiledScript.Cache

#### Level IV

| Identity | Value |
| --- | --- |
| Id | HandCannon_SingleAction_01_Level4 |
| Level | 4 |
| Level label | IV |
| Variant | Standard |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 40 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 40 |
| Firearm critical/headshot multiplier | 2.5 |
| ARC armour multiplier | 1.5 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 70 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 6 |
| Reload time stat, seconds | 2.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.003733 |
| Base partial-reload duration, seconds | — |
| Uses shell/looping reload | Yes |
| Base shell-reload entry, seconds | 0.8 |
| Base shell-reload loop, seconds | 0.7 |
| Base shell-reload exit, seconds | 0.55 |
| Shells loaded per loop | 1 |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 40 | 40 |
| Armor | 0.6 | 0.4 | 1.5 | 1 | 0.6 | 24 | 24 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 16 | 16 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 60 | 60 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 60 | 60 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 48 | 48 |

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
| Damage | 40 |
| Fire rate | 10.333 |
| Range | 50.21 |
| Stability | 67.769 |
| Agility | 70.105 |
| Stealth | 10 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Curve_DamageFalloff_HandCannon_SingleAction_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
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

###### Firerate

| Field | Value |
| --- | --- |
| Add | 20 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Dispersionrecoveryspeed

| Field | Value |
| --- | --- |
| Add | -0.5 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/BP_Item_HandCannon_SingleAction_01.json |
| Item | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/DA_Item_HandCannon_SingleAction_01.json |
| Quality set | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/BP_WeaponQualitySet_HandCannon_SingleAction_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/BP_WeaponQualitySet_HandCannon_SingleAction_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/BP_Projectile_HandCannon_SingleAction_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/BP_Item_HandCannon_SingleAction_01.json, Script/PrecompiledScript.Cache

### Amplified configurations

| Level / variant | Damage / projectile | Projectiles | Full spread | Crit × | ARC armour × | ARC weakpoint × | RPM | Magazine | Reload stat, s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Default | 40 | 1 | 40 | 2.5 | 1.5 | 1 | 70 | 6 | 2.5 |
| Anvil Splitter | 12 | 4 | 48 | 1.5 | 1.5 | 1 | 70 | 6 | 2.5 |
| X-Rounds | 45 | 1 | 45 | 2.25 | 2 | 1 | 70 | 6 | 2.5 |

#### Amplified — Default

| Identity | Value |
| --- | --- |
| Id | HandCannon_SingleAction_01_Ascended |
| Level | 5 |
| Level label | Amplified |
| Variant | Default |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 40 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 40 |
| Firearm critical/headshot multiplier | 2.5 |
| ARC armour multiplier | 1.5 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 70 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 6 |
| Reload time stat, seconds | 2.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.001867 |
| Base partial-reload duration, seconds | — |
| Uses shell/looping reload | Yes |
| Base shell-reload entry, seconds | 0.8 |
| Base shell-reload loop, seconds | 0.7 |
| Base shell-reload exit, seconds | 0.55 |
| Shells loaded per loop | 1 |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 40 | 40 |
| Armor | 0.6 | 0.4 | 1.5 | 1 | 0.6 | 24 | 24 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 16 | 16 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 60 | 60 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 60 | 60 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 48 | 48 |

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
| Damage | 40 |
| Fire rate | 10.333 |
| Range | 50.21 |
| Stability | 67.769 |
| Agility | 70.105 |
| Stealth | 10 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Curve_DamageFalloff_HandCannon_SingleAction_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
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

###### Firerate

| Field | Value |
| --- | --- |
| Add | 20 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Dispersionrecoveryspeed

| Field | Value |
| --- | --- |
| Add | -0.5 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/BP_Item_HandCannon_SingleAction_01_Ascended.json |
| Item | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/DA_Item_HandCannon_SingleAction_01_Ascended.json |
| Quality set | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/BP_WeaponQualitySet_HandCannon_SingleAction_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/BP_WeaponQualitySet_HandCannon_SingleAction_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/BP_Projectile_HandCannon_SingleAction_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/BP_Item_HandCannon_SingleAction_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | HandCannon_SingleAction_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/Upgrades/DA_Upgrade_HandCannon_SingleAction_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Anvil Splitter

| Identity | Value |
| --- | --- |
| Id | HandCannon_SingleAction_01_ProjectileSplitter |
| Level | 5 |
| Level label | Amplified |
| Variant | Anvil Splitter |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 12 |
| Projectiles / simultaneous shot | 4 |
| Physical damage / full spread | 48 |
| Firearm critical/headshot multiplier | 1.5 |
| ARC armour multiplier | 1.5 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 70 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 6 |
| Reload time stat, seconds | 2.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.001867 |
| Base partial-reload duration, seconds | — |
| Uses shell/looping reload | Yes |
| Base shell-reload entry, seconds | 0.8 |
| Base shell-reload loop, seconds | 0.7 |
| Base shell-reload exit, seconds | 0.55 |
| Shells loaded per loop | 1 |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 12 | 48 |
| Armor | 0.6 | 0.4 | 1.5 | 1 | 0.6 | 7.2 | 28.8 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 4.8 | 19.2 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 18 | 72 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 18 | 72 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 14.4 | 57.6 |

##### Upgrades

###### Anvil Splitter

| Field | Value |
| --- | --- |
| Id | HandCannon_SingleAction_01_ProjectileSplitter |
| Name | Anvil Splitter |
| Description | Replaces the Anvil's bullets with rounds that split into four weaker projectiles. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/Upgrades/DA_Upgrade_HandCannon_SingleAction_01_ProjectileSplitter.json |
| Modifier source path | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/Upgrades/BP_UpgradeWeaponMod_HandCannon_SingleAction_01_ProjectileSplitter.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/Upgrades/BP_UpgradeWeaponMod_HandCannon_SingleAction_01_ProjectileSplitter.uasset |
| Modifier selection | baked_cache_enabled |

**Modifiers**

**Physicaldamage**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1 |
| Multiply | 0.3 |

**Criticaldamagemultiplier**

| Field | Value |
| --- | --- |
| Add | -1 |
| Addmultiply | 1 |
| Multiply | 1 |

**Dispersionrecoveryspeed**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.1 |
| Multiply | 1 |

**Basedispersion**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

**Velocitydispersionmax**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0 |
| Multiply | 1 |

**Zoomdispersionscale**

| Field | Value |
| --- | --- |
| Add | 0.4 |
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
| Damage | 48 |
| Fire rate | 10.333 |
| Range | 44.567 |
| Stability | 67.769 |
| Agility | 74.299 |
| Stealth | 10 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Curve_DamageFalloff_HandCannon_SingleAction_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
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

###### Firerate

| Field | Value |
| --- | --- |
| Add | 20 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Dispersionrecoveryspeed

| Field | Value |
| --- | --- |
| Add | -0.5 |
| Addmultiply | 0.1 |
| Multiply | 1 |

###### Physicaldamage

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1 |
| Multiply | 0.3 |

###### Criticaldamagemultiplier

| Field | Value |
| --- | --- |
| Add | -1 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Basedispersion

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Velocitydispersionmax

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0 |
| Multiply | 1 |

###### Zoomdispersionscale

| Field | Value |
| --- | --- |
| Add | 0.4 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/Permutations/BP_Item_HandCannon_SingleAction_01_ProjectileSplitter.json |
| Item | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/Permutations/DA_Item_HandCannon_SingleAction_01_ProjectileSplitter.json |
| Quality set | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/BP_WeaponQualitySet_HandCannon_SingleAction_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/BP_WeaponQualitySet_HandCannon_SingleAction_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/BP_Projectile_HandCannon_SingleAction_01_ProjectileSplitter.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/Permutations/BP_Item_HandCannon_SingleAction_01_ProjectileSplitter.json, Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/BP_Item_HandCannon_SingleAction_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | HandCannon_SingleAction_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/Upgrades/DA_Upgrade_HandCannon_SingleAction_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — X-Rounds

| Identity | Value |
| --- | --- |
| Id | HandCannon_SingleAction_01_XRounds |
| Level | 5 |
| Level label | Amplified |
| Variant | X-Rounds |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 45 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 45 |
| Firearm critical/headshot multiplier | 2.25 |
| ARC armour multiplier | 2 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 70 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 6 |
| Reload time stat, seconds | 2.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.001867 |
| Base partial-reload duration, seconds | — |
| Uses shell/looping reload | Yes |
| Base shell-reload entry, seconds | 0.8 |
| Base shell-reload loop, seconds | 0.7 |
| Base shell-reload exit, seconds | 0.55 |
| Shells loaded per loop | 1 |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 45 | 45 |
| Armor | 0.6 | 0.4 | 2 | 1 | 0.8 | 36 | 36 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 18 | 18 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 67.5 | 67.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 67.5 | 67.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 54 | 54 |

##### Upgrades

###### X-Rounds

| Field | Value |
| --- | --- |
| Id | HandCannon_SingleAction_01_XRounds |
| Name | X-Rounds |
| Description | Adds an explosive compound to the projectile, dealing slightly increased damage to Raiders and significantly increased damage to ARC Armor plating. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/Upgrades/DA_Upgrade_HandCannon_SingleAction_01_XRounds.json |
| Modifier source path | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/Upgrades/BP_UpgradeWeaponMod_HandCannon_SingleAction_01_XRounds.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/Upgrades/BP_UpgradeWeaponMod_HandCannon_SingleAction_01_XRounds.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Physicaldamage**

| Field | Value |
| --- | --- |
| Add | 5 |
| Addmultiply | 1 |
| Multiply | 1 |

**Launchspeed**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.5 |
| Multiply | 1 |

**Verticalrecoil**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.3 |
| Multiply | 1 |

**Horizontalrecoil**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.3 |
| Multiply | 1 |

**Criticaldamagemultiplier**

| Field | Value |
| --- | --- |
| Add | -0.25 |
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
| Fire rate | 10.333 |
| Range | 39.41 |
| Stability | 57.696 |
| Agility | 70.105 |
| Stealth | 5 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Curve_DamageFalloff_HandCannon_SingleAction_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
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

###### Firerate

| Field | Value |
| --- | --- |
| Add | 20 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Dispersionrecoveryspeed

| Field | Value |
| --- | --- |
| Add | -0.5 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Physicaldamage

| Field | Value |
| --- | --- |
| Add | 5 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Launchspeed

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.5 |
| Multiply | 1 |

###### Verticalrecoil

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.3 |
| Multiply | 1 |

###### Horizontalrecoil

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.3 |
| Multiply | 1 |

###### Criticaldamagemultiplier

| Field | Value |
| --- | --- |
| Add | -0.25 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/Permutations/BP_Item_HandCannon_SingleAction_01_XRounds.json |
| Item | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/Permutations/DA_Item_HandCannon_SingleAction_01_XRounds.json |
| Quality set | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/BP_WeaponQualitySet_HandCannon_SingleAction_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/BP_WeaponQualitySet_HandCannon_SingleAction_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/BP_Projectile_HandCannon_SingleAction_01_XRounds.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/Permutations/BP_Item_HandCannon_SingleAction_01_XRounds.json, Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/BP_Item_HandCannon_SingleAction_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | HandCannon_SingleAction_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/Upgrades/DA_Upgrade_HandCannon_SingleAction_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

<details>
<summary>Actual game source files</summary>

- [Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/BP_Item_HandCannon_SingleAction_01_Ascended.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/BP_Item_HandCannon_SingleAction_01_Ascended.json)
- [Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/BP_Projectile_HandCannon_SingleAction_01_ProjectileSplitter.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/BP_Projectile_HandCannon_SingleAction_01_ProjectileSplitter.json)
- [Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/BP_Projectile_HandCannon_SingleAction_01_XRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/BP_Projectile_HandCannon_SingleAction_01_XRounds.json)
- [Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/DA_Item_HandCannon_SingleAction_01_Ascended.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/DA_Item_HandCannon_SingleAction_01_Ascended.json)
- [Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/Permutations/BP_Item_HandCannon_SingleAction_01_ProjectileSplitter.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/Permutations/BP_Item_HandCannon_SingleAction_01_ProjectileSplitter.json)
- [Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/Permutations/BP_Item_HandCannon_SingleAction_01_XRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/Permutations/BP_Item_HandCannon_SingleAction_01_XRounds.json)
- [Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/Permutations/DA_Item_HandCannon_SingleAction_01_ProjectileSplitter.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/Permutations/DA_Item_HandCannon_SingleAction_01_ProjectileSplitter.json)
- [Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/Permutations/DA_Item_HandCannon_SingleAction_01_XRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/Permutations/DA_Item_HandCannon_SingleAction_01_XRounds.json)
- [Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/Upgrades/BP_UpgradeWeaponMod_HandCannon_SingleAction_01_ProjectileSplitter.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/Upgrades/BP_UpgradeWeaponMod_HandCannon_SingleAction_01_ProjectileSplitter.json)
- [Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/Upgrades/BP_UpgradeWeaponMod_HandCannon_SingleAction_01_XRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/Upgrades/BP_UpgradeWeaponMod_HandCannon_SingleAction_01_XRounds.json)
- [Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/Upgrades/DA_Upgrade_HandCannon_SingleAction_01_Ascended.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/Upgrades/DA_Upgrade_HandCannon_SingleAction_01_Ascended.json)
- [Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/Upgrades/DA_Upgrade_HandCannon_SingleAction_01_ProjectileSplitter.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/Upgrades/DA_Upgrade_HandCannon_SingleAction_01_ProjectileSplitter.json)
- [Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/Upgrades/DA_Upgrade_HandCannon_SingleAction_01_XRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/Upgrades/DA_Upgrade_HandCannon_SingleAction_01_XRounds.json)
- [Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/BP_Item_HandCannon_SingleAction_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/BP_Item_HandCannon_SingleAction_01.json)
- [Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/BP_Projectile_HandCannon_SingleAction_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/BP_Projectile_HandCannon_SingleAction_01.json)
- [Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/BP_WeaponQualitySet_HandCannon_SingleAction_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/BP_WeaponQualitySet_HandCannon_SingleAction_01.json)
- [Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Curve_DamageFalloff_HandCannon_SingleAction_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Curve_DamageFalloff_HandCannon_SingleAction_01.json)
- [Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/DA_Item_HandCannon_SingleAction_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/DA_Item_HandCannon_SingleAction_01.json)

</details>
