project "croaring"

dofile(_BUILD_DIR .. "/static_library.lua")

configuration { "*" }

uuid "C8804B2B-1A46-4E89-955A-92AEFB6CDBB3"

includedirs {
  "cpp",
  "include",
}

files {
  "src/*.c",
  "src/containers/*.c",
}

if (_PLATFORM_ANDROID) then
end

if (_PLATFORM_IOS) then
end

if (_PLATFORM_LINUX) then
end

if (_PLATFORM_MACOS) then
end

if (_PLATFORM_WINDOWS) then
end

if (_PLATFORM_WINUWP) then
end
