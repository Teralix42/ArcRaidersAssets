# Tempest

[Weapons](README.md) · [Mechanics](Mechanics.md) · [ARC damage model](../ARC/Damage_Model.md)

**Ammo:** Medium · **Game ID:** `AssaultRifle_Bullpup_01`

[Weapon blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Bullpup_01/BP_Item_AssaultRifle_Bullpup_01.json) · [Item config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Bullpup_01/DA_Item_AssaultRifle_Bullpup_01.json) · [Level modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Bullpup_01/BP_WeaponQualitySet_AssaultRifle_Bullpup_01.json) · [Projectile](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Bullpup_01/BP_Projectile_AssaultRifle_Bullpup_01.json)

### Level I

| Stat | Value |
| --- | --- |
| Body damage / projectile | 10 |
| Headshot multiplier | 1.5× |
| ARC armor multiplier | 0.8× |
| ARC weak-point multiplier | 1× |
| Fire rate (RPM) | 550 |
| Magazine | 25 |
| Reload stat (s) | 3.75 |
| Firing mode | Full-auto |
| ARC armor propagation multiplier | 0.4× |
| Durability burn rate | 0.001056 |
| Partial-reload base duration (s) | 2.57333 |

### Level II–IV changes

All deltas are relative to Level I. A dash means unchanged.

| Level | Reload stat (s) | Durability burn rate | Handling modifiers |
| --- | --- | --- | --- |
| II | −0.5 | −0.000106 | −16.666667% horizontal recoil |
| III | −1 | −0.000211 | −33.333333% horizontal recoil |
| IV | −1.5 | −0.000317 | −50% horizontal recoil |

### Direct physical damage to ARC

Baseline damage per projectile at full exposure, before falloff and damage propagation. [ARC damage model](../ARC/Damage_Model.md)

| Part group | Damage |
| --- | --- |
| Normal | 10 |
| Armor | 3.2 |
| Sturdy | 4 |
| WeakPoint | 15 |
| Critical | 15 |
| Fragile | 12 |

### Damage falloff

| Distance (m) | Damage factor | Interpolation |
| --- | --- | --- |
| 0 | 1.2× | Linear |
| 5 | 1.2× | Linear |
| 15 | 1.001× | Linear |
| 150 | 1.001× | Linear |
| 170 | 0.6× | Linear |

[Game curve](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Bullpup_01/Curve_DamageFalloff_AssaultRifle_Bullpup_01.json)
