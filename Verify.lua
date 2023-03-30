game.ReplicatedStorage.Verify.OnClientEvent:Connect(function(tnum)
	game.StarterGui:SetCore( "ChatMakeSystemMessage",  { Text = "Verification Code:" .. tnum, Color = Color3.fromRGB(0, 255, 255), Font = Enum.Font.Arial, FontSize = Enum.FontSize.Size24 } )
end)
