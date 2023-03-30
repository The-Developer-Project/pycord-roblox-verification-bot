local HttpService = game:GetService("HttpService")
local url = "url"
game.Players.PlayerAdded:Connect(function(player)
	player.Chatted:Connect(function(msg)
		if msg == "/link" then
			local tnum = tostring(math.random(1,10000000))
			local token = tnum .. '+' .. player.Name
			HttpService:PostAsync(url, token)
			game.ReplicatedStorage.Verify:FireClient(player, tnum)
		end
	end)
end)
