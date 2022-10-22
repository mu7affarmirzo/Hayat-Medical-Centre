import "@mui/material/styles";
import "@mui/material/Typography";

declare module '@mui/material/styles' {
    interface TypographyVariants {
        interFont: React.CSSProperties;
    }

    // allow configuration using `createTheme`
    interface TypographyVariantsOptions {
        interFont?: React.CSSProperties;
    }
}

// Update the Typography's variant prop options
declare module '@mui/material/Typography' {
    interface TypographyPropsVariantOverrides {
        interFont: true;
    }
}
