# Torrente

[Weapons](README.md) · [Mechanics](Mechanics.md) · [ARC damage model](../ARC/Damage_Model.md)

**Ammo:** Medium · **Game ID:** `LMG_Medium_01`

[Weapon blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/LMG_Medium_01/BP_Item_LMG_Medium_01.json) · [Item config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/LMG_Medium_01/DA_Item_LMG_Medium_01.json) · [Level modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/LMG_Medium_01/BP_WeaponQualitySet_LMG_Medium_01.json) · [Projectile](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/LMG_Medium_01/BP_Projectile_LMG_Medium_01.json)

[Timing fields and game-code formulas](Mechanics.md#firing-and-reload-timers).

### Level I

| Stat | Value |
| --- | --- |
| Body damage / projectile | 8 |
| Headshot multiplier | 2× |
| ARC armor multiplier | 1× |
| ARC weak-point multiplier | 1× |
| Configured fire rate (RPM) | 800 |
| RPM interval (s) | 0.075 |
| Magazine | 60 |
| Reload stat (s) | 8 |
| Firing mode | Full-auto |
| ARC armor propagation multiplier | 0.4× |
| Durability burn rate | 0.000899 |
| Partial-reload base duration (s) | 5 |

### Level II–IV changes

All deltas are relative to Level I. A dash means unchanged.

| Level | Magazine | Reload stat (s) | Durability burn rate |
| --- | --- | --- | --- |
| II | +10 | −1 | −9e−05 |
| III | +20 | −2 | −0.00018 |
| IV | +30 | −3 | −0.00027 |

### Direct physical damage to ARC

Baseline damage per projectile at full exposure, before falloff and damage propagation. [ARC damage model](../ARC/Damage_Model.md)

| Part group | Damage |
| --- | --- |
| Normal | 8 |
| Armor | 3.2 |
| Sturdy | 3.2 |
| WeakPoint | 12 |
| Critical | 12 |
| Fragile | 9.6 |

### Damage falloff

| Distance (m) | Damage factor | Interpolation |
| --- | --- | --- |
| 0 | 1.001× | Linear |
| 15 | 1.001× | Linear |
| 150 | 1.001× | Linear |
| 170 | 0.6× | Linear |

[Game curve](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/LMG_Medium_01/Curve_DamageFalloff_LMG_Medium_01.json)
