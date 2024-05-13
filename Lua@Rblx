local contentProvider = game:GetService("ContentProvider")
local ui = script:WaitForChild("ScreenGui"):Clone()

repeat wait() until game:IsLoaded()

local assets = game:GetDescendants()
local maxAssets = #assets

local playr = game.Players.LocalPlayer
local playrGui = playr:WaitForChild("PlayerGui")

ui.Parent = playrGui -- LOADING BEGAN

for i, assetToLoad in assets do
	wait(0.001) ---> *(change this accoring to preference)*
	contentProvider:PreloadAsync({assetToLoad})
	ui:WaitForChild("Frame"):WaitForChild("TextLabel").Text = i.."/"..maxAssets
end

ui:Destroy() -- LOADING ENDED

