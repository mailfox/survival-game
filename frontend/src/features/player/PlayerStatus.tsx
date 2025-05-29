import React, { useEffect, useState } from 'react'
import { PlayerStats } from './playerTypes'

export const PlayerStatus = ({ playerId }: { playerId: number }) => {
  const [stats, setStats] = useState<PlayerStats>({
    health: 100,
    hunger: 100,
    thirst: 100,
    radiation: 0
  })

  useEffect(() => {
    const fetchStats = async () => {
      const response = await fetch(`/api/v1/player/status/${playerId}`)
      const data = await response.json()
      setStats(data)
    }
    
    fetchStats()
    const interval = setInterval(fetchStats, 10000)
    return () => clearInterval(interval)
  }, [playerId])

  return (
    <div className="player-status">
      <StatBar label="Health" value={stats.health} max={100} color="red" />
      <StatBar label="Hunger" value={stats.hunger} max={100} color="orange" />
      <StatBar label="Thirst" value={stats.thirst} max={100} color="blue" />
      {stats.radiation > 0 && (
        <StatBar label="Radiation" value={stats.radiation} max={100} color="purple" />
      )}
    </div>
  )
}