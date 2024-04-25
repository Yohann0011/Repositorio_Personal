<<<<<<< HEAD
//========================================================================
//
// SplashGlyphBitmap.h
//
//========================================================================

#ifndef SPLASHGLYPHBITMAP_H
#define SPLASHGLYPHBITMAP_H

//------------------------------------------------------------------------
// SplashGlyphBitmap
//------------------------------------------------------------------------

struct SplashGlyphBitmap
{
    int x, y, w, h; // offset and size of glyph
    bool aa; // anti-aliased: true means 8-bit alpha
             //   bitmap; false means 1-bit
    unsigned char *data; // bitmap data
    bool freeData; // true if data memory should be freed
};

#endif
=======
//========================================================================
//
// SplashGlyphBitmap.h
//
//========================================================================

#ifndef SPLASHGLYPHBITMAP_H
#define SPLASHGLYPHBITMAP_H

//------------------------------------------------------------------------
// SplashGlyphBitmap
//------------------------------------------------------------------------

struct SplashGlyphBitmap
{
    int x, y, w, h; // offset and size of glyph
    bool aa; // anti-aliased: true means 8-bit alpha
             //   bitmap; false means 1-bit
    unsigned char *data; // bitmap data
    bool freeData; // true if data memory should be freed
};

#endif
>>>>>>> 8086880b55efd63f49e0728f2f4fa0b85da2c170
