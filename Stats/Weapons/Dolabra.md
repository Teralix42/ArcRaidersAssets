# Dolabra

[Weapons](README.md) · [Mechanics](Mechanics.md) · [ARC damage model](../ARC/Damage_Model.md)

**Ammo:** Energy · **Game ID:** `Shotgun_Energy_Adjustable_01`

[Weapon blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_Energy_Adjustable_01/BP_Item_Shotgun_Energy_Adjustable_01.json) · [Item config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_Energy_Adjustable_01/DA_Item_Shotgun_Energy_Adjustable_01.json) · [Projectile](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_Energy_Adjustable_01/BP_Projectile_Shotgun_Energy_Adjustable_01.json)

### Standard

| Stat | Value |
| --- | --- |
| Configured physical damage (hit-normalized) | 25 |
| Headshot multiplier | 1× |
| ARC armor multiplier | 1.5× |
| ARC weak-point multiplier | 1.5× |
| Fire rate (RPM) | 55 |
| Magazine | 8 |
| Reload stat (s) | 3.25 |
| Firing mode | Semi-auto |
| Projectiles per shot | 19 |
| ARC armor propagation multiplier | 1.5× |
| Durability burn rate | 0.003582 |
| Partial-reload base duration (s) | 3.25 |

### Firing, reload and impact details

- Hits required for full damage **2**
- Damage is hit-normalized. Multiplying the listed damage by every projectile would overstate a full spread.

### Damage falloff

| Distance (m) | Damage factor | Interpolation |
| --- | --- | --- |
| 0 | 1.001× | Linear |
| 20 | 1.001× | Linear |
| 100 | 0.8× | Linear |

[Game curve](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_Energy_Adjustable_01/Curve_DamageFalloff_Shotgun_Energy_Adjustable_01.json)
